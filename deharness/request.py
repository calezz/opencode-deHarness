"""Mint AND drive opencode free-tier sessions from pure Python. Returns objects.
Verified live end-to-end (mint 200, chained memory recall works).
Two rules the gate enforces (both proven by test):
1. session ID in exact client format (schema/session-id.ts + identifier.ts):
   ses_ + 12 hex time chars + 14 random base62 chars (bare random IDs 403)
2. full body shape (full instructions/tools; trimmed bodies 403)
Self-contained: needs only template-main-body.json beside this file
(main-turn keys; history stripped). Per-session state lives in
session-<ses_...>.json files next to it.
"""
import json
import os
import secrets
import time

import requests

UPSTREAM = "https://opencode.ai"
# Endpoint paths: protocol contract, not configuration. The gate routes and
# validates on these exact paths - they are named (not inline) so a typo can
# never silently diverge them, but they are never user-settable.
PATH_RESPONSES = "/inference/v1/responses"
PATH_MODELS = "/inference/v1/models"
PATH_SYSTEMONE = "/inference/v1/systemone"
MODEL = "muse-spark-1.3-contributor-free"
TIMEOUT = 180
MODELS_TIMEOUT = 30
EVAL_TIMEOUT = 60
CLIENT_VERSION = "2.0.29"
RETRIES = 2
RETRY_DELAY = 1.0
REASONING_EFFORT = "xhigh"
ID_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
_HERE = os.path.dirname(os.path.abspath(__file__))

TITLE_INSTRUCTIONS = """You are a title generator. You output ONLY a thread title. Nothing else.

<task>
Generate a brief title that would help the user find this conversation later.

Follow all rules in <rules>
Use the <examples> so you know what a good title looks like.
Your output must be:
- A single line
- <=50 characters
- No explanations
</task>

<rules>
- you MUST use the same language as the user message you are summarizing
- Title must be grammatically correct and read naturally - no word salad
- Never include tool names in the title (e.g. "read tool", "bash tool", "edit tool")
- Focus on the main topic or question the user needs to retrieve
- Vary your phrasing - avoid repetitive patterns like always starting with "Analyzing"
- When a file is mentioned, focus on WHAT the user wants to do WITH the file, not just that they shared it
- Keep exact: technical terms, numbers, filenames, HTTP codes
- Remove: the, this, my, a, an
- Never assume tech stack
- Never use tools
- NEVER respond to questions, just generate a title for the conversation
- The title should NEVER include "summarizing" or "generating" when generating a title
- DO NOT SAY YOU CANNOT GENERATE A TITLE OR COMPLAIN ABOUT THE INPUT
- Always output something meaningful, even if the input is minimal.
- If the user message is short or conversational (e.g. "hello", "lol", "what's up", "hey"):
  -> create a title that reflects the user's tone or intent (such as Greeting, Quick check-in, Light chat, Intro message, etc.)
</rules>

<examples>
"debug 500 errors in production" -> Debugging production 500 errors
"refactor user service" -> Refactoring user service
"why is app.js failing" -> app.js failure investigation
"implement rate limiting" -> Rate limiting implementation
"how do I connect postgres to my API" -> Postgres API connection
"best practices for React hooks" -> React hooks best practices
"@src/credential.ts can you add refresh token support" -> Credential refresh token support
"@utils/parser.ts this is broken" -> Parser bug fix
"look at @config.json" -> Config review
"@App.tsx add dark mode toggle" -> Dark mode toggle in App
</examples>"""


def mint_session_id() -> str:
    current = int(time.time() * 1000) * 0x1000 + 1
    value = (~current) & 0xFFFFFFFFFFFF
    head = "".join(f"{(value >> (40 - 8 * i)) & 0xFF:02x}" for i in range(6))
    tail = "".join(ID_CHARS[secrets.randbelow(62)] for _ in range(14))
    return "ses_" + head + tail


def _headers(session_id: str, project_id: str) -> dict:
    trace, span = secrets.token_hex(16), secrets.token_hex(8)
    return {
        "Authorization": "Bearer public",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "User-Agent": f"opencode/latest/{CLIENT_VERSION}/desktop",
        "b3": f"{trace}-{span}-1-0000000000000001",
        "traceparent": f"00-{trace}-{span}-01",
        "x-opencode-client": "desktop",
        "x-opencode-project": project_id,
        "x-opencode-session": session_id,
        "x-opencode-session-id": session_id,
        "x-session-affinity": session_id,
        "x-session-id": session_id,
    }


def _proxy_url(proxy: str) -> str:
    """requests proxy URL for a proxy string. Standalone (no pool import) so
    this package installs and runs with nothing else: bare host:port -> http,
    socks5 -> socks5h (remote DNS, needed for region-blocked hosts),
    socks4 -> socks4a, anything else passes through unchanged."""
    if proxy.startswith("socks5://"):
        return "socks5h://" + proxy[len("socks5://"):]
    if proxy.startswith("socks4://"):
        return "socks4a://" + proxy[len("socks4://"):]
    if "://" in proxy:
        return proxy
    return f"http://{proxy}"


def _via(proxy: str) -> dict:
    url = _proxy_url(proxy)
    return {"http": url, "https": url}


def _resolve_model(model: str | None) -> str:
    m = MODEL if model is None else model
    if not isinstance(m, str) or not m.strip():
        raise ValueError("model must be a non-empty string")
    return m


def _resolve_timeout(timeout, default: float = TIMEOUT) -> float:
    t = default if timeout is None else timeout
    try:
        t = float(t)
    except (TypeError, ValueError):
        raise ValueError("timeout must be a positive number of seconds")
    if t <= 0:
        raise ValueError("timeout must be a positive number of seconds")
    return t


def _resolve_retries(retries) -> int:
    n = RETRIES if retries is None else retries
    try:
        n = int(n)
    except (TypeError, ValueError):
        raise ValueError("retries must be an integer >= 0")
    if n < 0:
        raise ValueError("retries must be an integer >= 0")
    return n


def _resolve_delay(delay) -> float:
    d = RETRY_DELAY if delay is None else delay
    try:
        d = float(d)
    except (TypeError, ValueError):
        raise ValueError("retry_delay must be a number >= 0")
    if d < 0:
        raise ValueError("retry_delay must be a number >= 0")
    return d


def _template_path(files_dir: str) -> str:
    """Chain template lookup: the caller's dir wins so customized templates
    keep working; the packaged copy is the fallback so a bare working
    directory works out of the box."""
    candidate = os.path.join(files_dir, "template-main-body.json")
    if os.path.exists(candidate):
        return candidate
    return os.path.join(_HERE, "template-main-body.json")


def _send(path: str, headers: dict, body: dict, proxy: str | None = None,
          timeout=None, retries=None, retry_delay=None,
          model: str | None = None) -> dict:
    # An explicit model stamps the outgoing body (on a copy - the caller's
    # dict is never mutated) and the report. Omitted, the body stands as
    # given. Same one-turn-override pattern as continue_session.
    if model is not None:
        body = dict(body)
        body["model"] = _resolve_model(model)
    out: dict = {"status": 0, "id": None, "model": body.get("model"),
                 "text": "", "usage": None, "error": None,
                 "proxy": proxy, "proxy_country": None}
    output_items: list = []
    proxies = _via(proxy) if proxy else None
    out["via"] = proxy
    timeout_s = _resolve_timeout(timeout)
    attempts = 1 + _resolve_retries(retries)
    delay_s = _resolve_delay(retry_delay)
    # Bounded same-proxy retry: transport blips only (connection reset,
    # timeout, proxy drop). HTTP statuses - including 429/403 - are answers,
    # returned immediately, never retried. No pool switching here; that lives
    # in via_pool.py.
    response = None
    last_exc: Exception | None = None
    for attempt in range(attempts):
        if attempt > 0 and delay_s > 0:
            time.sleep(delay_s)
        try:
            response = requests.post(UPSTREAM + path, headers=headers, json=body,
                                     timeout=timeout_s, stream=True, proxies=proxies)
            break
        except Exception as e:  # noqa: BLE001
            last_exc = e
            response = None
            continue
    if response is None:
        out["error"] = (f"proxy failed: {last_exc}" if proxy
                        else str(last_exc)[:300])
        return out
    with response as r:
        out["status"] = r.status_code
        if r.status_code != 200:
            out["error"] = r.text[:300]
            # A model that does not speak this protocol (e.g. continuing a
            # responses-protocol chain on a chat-completions model) fails with
            # a specific type. Mark it so callers can tell "wrong protocol"
            # apart from quota/transport failures without string-matching.
            # Key is absent on every other outcome - old shapes unchanged.
            try:
                if "ModelProtocolUnsupported" in (out["error"] or ""):
                    out["error_kind"] = "model-protocol-unsupported"
            except Exception:  # noqa: BLE001
                pass
            return out
        for line in r.iter_lines(decode_unicode=True):
            if not line or not line.startswith("data:"):
                continue
            try:
                event = json.loads(line[5:])
            except ValueError:
                continue
            kind = event.get("type")
            if kind == "response.output_text.delta":
                out["text"] += event.get("delta", "")
            elif kind == "response.completed":
                resp = event.get("response", {})
                out["id"] = resp.get("id", out["id"])
                out["model"] = resp.get("model", out["model"])
                out["usage"] = resp.get("usage", out["usage"])
                output_items = resp.get("output", [])
                if not out["text"]:
                    for item in output_items:
                        for part in item.get("content", []):
                            if part.get("type") == "output_text":
                                out["text"] += part.get("text", "")
            elif kind in ("response.created", "response.in_progress") and not out["id"]:
                out["id"] = event.get("response", {}).get("id")
    out["output_items"] = output_items
    return out


def mint_session(first_text: str = "hello", proxy: str | None = None,
                 project_id: str | None = None, files_dir: str | None = None,
                 model: str | None = None, instructions: str | None = None,
                 reasoning_effort: str | None = None,
                 timeout=None, retries=None, retry_delay=None) -> dict:
    """Create a brand-new session like the client does, then seed its chain
    file. Returns {status, session_id, project_id, id, model, text, ...}.
    status 200 = minted and usable with continue_session().
    Session files live in files_dir (default: current working directory)."""
    files_dir = os.getcwd() if files_dir is None else files_dir
    sid = mint_session_id()
    pid = project_id or secrets.token_hex(20)
    resolved_model = _resolve_model(model)
    resolved_effort = (REASONING_EFFORT if reasoning_effort is None
                       else reasoning_effort)
    if not isinstance(resolved_effort, str) or not resolved_effort.strip():
        raise ValueError("reasoning_effort must be a non-empty string")
    body = {
        "model": resolved_model,
        "input": [{"type": "message", "role": "user",
                   "content": [{"type": "input_text", "text": first_text}]}],
        "instructions": TITLE_INSTRUCTIONS if instructions is None else instructions,
        "stream": True,
        "store": False,
        "prompt_cache_key": sid,
        "include": ["reasoning.encrypted_content"],
        "reasoning": {"effort": resolved_effort, "summary": "auto"},
    }
    out = _send(PATH_RESPONSES, _headers(sid, pid), body, proxy,
                timeout=timeout, retries=retries, retry_delay=retry_delay)
    out["session_id"], out["project_id"] = sid, pid
    if out["status"] == 200:
        with open(_template_path(files_dir), encoding="utf-8") as f:
            main_base = dict(json.load(f))
        main_base["prompt_cache_key"] = sid
        main_base["model"] = resolved_model
        if isinstance(main_base.get("reasoning"), dict):
            main_base["reasoning"] = dict(main_base["reasoning"])
            main_base["reasoning"]["effort"] = resolved_effort
        main_base["input"] = [body["input"][0]]
        with open(os.path.join(files_dir, f"session-{sid}.json"), "w", encoding="utf-8") as f:
            json.dump({"path": PATH_RESPONSES, "headers": _headers(sid, pid),
                       "body": main_base, "project_id": pid}, f)
    return out


def continue_session(prompt: str, session_id: str, proxy: str | None = None,
                     files_dir: str | None = None, reasoning_effort: str | None = None,
                     timeout=None, retries=None, retry_delay=None,
                     model: str | None = None) -> dict:
    """Append a user turn on a minted session, extend the chain. Returns
    {"status", "id", "model", "text", "usage", "error", "chain_len"}.
    reasoning_effort / model override the chain's values for this turn only -
    the saved chain keeps the session defaults, so the next turn without
    overrides goes back to them. Switch models mid-chain freely."""
    files_dir = os.getcwd() if files_dir is None else files_dir
    with open(os.path.join(files_dir, f"session-{session_id}.json"), encoding="utf-8") as f:
        saved = json.load(f)
    full, headers = saved["body"], saved["headers"]
    body = dict(full)
    body["input"] = list(full["input"]) + [
        {"type": "message", "role": "user",
         "content": [{"type": "input_text", "text": prompt}]}]
    if reasoning_effort is not None:
        if not isinstance(reasoning_effort, str) or not reasoning_effort.strip():
            raise ValueError("reasoning_effort must be a non-empty string")
        if isinstance(body.get("reasoning"), dict):
            body["reasoning"] = dict(body["reasoning"])
            body["reasoning"]["effort"] = reasoning_effort
    if model is not None:
        body["model"] = _resolve_model(model)
    out = _send(saved["path"], headers, body, proxy,
                timeout=timeout, retries=retries, retry_delay=retry_delay)
    items = out.pop("output_items", [])
    out["chain_len"] = len(body["input"])
    if out["status"] == 200 and items:
        chained = dict(full)
        chained["input"] = body["input"] + items
        saved["body"] = chained
        with open(os.path.join(files_dir, f"session-{session_id}.json"), "w", encoding="utf-8") as f:
            json.dump(saved, f)
        out["chain_len"] = len(chained["input"])
    return out


def list_models(timeout=None) -> list:
    """Live catalog: GET /inference/v1/models (no auth needed).
    Returns sorted model IDs, e.g. muse-spark-1.3-contributor-free."""
    r = requests.get(UPSTREAM + PATH_MODELS,
                     timeout=_resolve_timeout(timeout, MODELS_TIMEOUT))
    r.raise_for_status()
    return sorted(m["id"] for m in r.json()["data"])


def evaluate(model: str, state: str, questions: dict,
             session_id: str | None = None,
             project_id: str | None = None, timeout=None) -> dict:
    """System One evaluation tier (Jev, TypeSafe AI): no text out, only
    structured answers + probabilities. POST /inference/v1/systemone.
    questions: {"qid": {"type": "noul"|"choice"|"score",
      "instructions": str, "criteria": {...} (choice/score only)}}.
    Free model jev-1.13-free needs no session. Returns
    {"status", "model", "answers", "usage", "error"}."""
    headers = {
        "Authorization": "Bearer public",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "User-Agent": f"opencode/latest/{CLIENT_VERSION}/desktop",
    }
    if session_id:
        headers.update({
            "x-opencode-client": "desktop",
            "x-opencode-project": project_id or "",
            "x-opencode-session": session_id,
            "x-opencode-session-id": session_id,
            "x-session-affinity": session_id,
            "x-session-id": session_id,
        })
    r = requests.post(UPSTREAM + PATH_SYSTEMONE, headers=headers,
                      json={"model": model, "state": state,
                            "questions": questions},
                      timeout=_resolve_timeout(timeout, EVAL_TIMEOUT))
    out: dict = {"status": r.status_code, "model": model,
                 "answers": None, "usage": None, "error": None}
    if r.status_code != 200:
        out["error"] = r.text[:300]
        return out
    data = r.json()
    out["model"], out["answers"], out["usage"] = \
        data.get("model"), data.get("answers"), data.get("usage")
    return out


if __name__ == "__main__":
    minted = mint_session("hello")
    print("mint:", minted["status"], minted.get("session_id"), repr(minted.get("text"))[:80])
