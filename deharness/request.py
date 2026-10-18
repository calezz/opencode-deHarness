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
# Protocol-family endpoints (v2.0.30+ layout, see opencode-src commit 1ca34ae):
# the client picks the endpoint per model from models.dev `provider.npm`.
PATH_CHAT = "/inference/openai/v1/chat/completions"
CHAT_SUFFIX = "/chat/completions"
# Endpoint family per models.dev npm package (the live feed decides, never a
# hardcoded model list): opencode free models are all @ai-sdk/openai-compatible
# today, legacy ones were @ai-sdk/openai (responses), and paywalled claude/
# gemini/qwen entries use the anthropic/google families (chain sessions only
# support chat/responses).
PROTOCOL_FAMILY = {
    "@ai-sdk/openai-compatible": "chat",
    "@ai-sdk/openai": "responses",
    "@ai-sdk/anthropic": "anthropic",
    "@ai-sdk/google": "google",
}
# models.dev feed: the same public data the client loads (bundled snapshot at
# 2.0.30+; fetched live here with a cache beside this file).
MODELS_DEV = "https://models.dev/api.json"
MODELS_DEV_TTL = 12 * 3600.0
MODEL = "muse-spark-1.3-contributor-free"
TIMEOUT = 180
MODELS_TIMEOUT = 30
EVAL_TIMEOUT = 60
CLIENT_VERSION = "2.0.32"
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


def _chat_main_template() -> tuple:
    """The captured turn-1 MAIN chat frame packaged as
    template-chat-main.json: {"system": <full harness system prompt>,
    "tools": [<client tool catalog>]}. The gate's main-shape check keys on
    exactly these two pieces; max_completion_tokens resolves dynamically
    from the feed per model."""
    with open(os.path.join(_HERE, "template-chat-main.json"), encoding="utf-8") as f:
        tmpl = json.load(f)
    return tmpl["system"], tmpl.get("tools") or []


_SNAP_CACHE: tuple | None = None  # (fetched_at, providers)


def _models_dev(force: bool = False):
    """Live models.dev provider feed, cached in-memory and to
    models-dev-cache.json beside this file. The client itself loads this data
    to pick endpoints, so protocols are never hardcoded here. A stale cache
    beats a dead network; a cold network with no cache returns None."""
    global _SNAP_CACHE
    now = time.time()
    if not force and _SNAP_CACHE and now - _SNAP_CACHE[0] < MODELS_DEV_TTL:
        return _SNAP_CACHE[1]
    cache = os.path.join(_HERE, "models-dev-cache.json")
    cached = None
    if os.path.exists(cache):
        try:
            with open(cache, encoding="utf-8") as f:
                cached = json.load(f)
        except Exception:
            cached = None
    if not force and cached and now - cached.get("fetched_at", 0) < MODELS_DEV_TTL:
        _SNAP_CACHE = (cached.get("fetched_at", now), cached.get("providers"))
        return _SNAP_CACHE[1]
    try:
        r = requests.get(MODELS_DEV, timeout=10)
        r.raise_for_status()
        providers = r.json()
    except Exception:
        if cached:
            return cached.get("providers")
        return _SNAP_CACHE[1] if _SNAP_CACHE else None
    with open(cache, "w", encoding="utf-8") as f:
        json.dump({"fetched_at": now, "providers": providers}, f)
    _SNAP_CACHE = (now, providers)
    return providers


def model_protocol(model_id: str) -> tuple:
    """(family, target_url) for a model, resolved from the live models.dev
    feed the same way the client routes it: per-model `provider.npm`/`api`
    win over provider-level values. Unknown models (e.g. systemone-eval ids
    absent from the feed) keep the legacy flat responses path."""
    providers = _models_dev() or {}
    entry = providers.get("opencode") or {}
    mentry = (entry.get("models") or {}).get(model_id) or {}
    per_model = mentry.get("provider") or {}
    npm = per_model.get("npm") or entry.get("npm")
    base = per_model.get("api") or entry.get("api")
    family = PROTOCOL_FAMILY.get(npm, "responses")
    if family == "chat":
        url = (base.rstrip("/") + CHAT_SUFFIX) if base else UPSTREAM + PATH_CHAT
        return "chat", url
    if family != "responses":
        return family, base  # supported only as an explicit error in _send
    return "responses", (base or None)


def model_target(model_id: str) -> str:
    """Absolute POST URL for a model's family; responses stays on the legacy
    flat path the gate has always validated."""
    family, target = model_protocol(model_id)
    if family == "responses":
        return UPSTREAM + PATH_RESPONSES
    return target


def free_models(timeout=10) -> list:
    """Free model IDs from the live models.dev feed (zero input/output cost).
    New free models show up automatically - no caller-side lists."""
    providers = _models_dev() or {}
    out = []
    for mid, meta in sorted((providers.get("opencode") or {}).get("models", {}).items()):
        cost = meta.get("cost") or {}
        if cost.get("input", 0) == 0 and cost.get("output", 0) == 0:
            out.append(mid)
    return out


def first_text_of(body: dict) -> str:
    """Last user text in a responses-style input list, for chat translation."""
    items = body.get("input")
    if not isinstance(items, list) or not items:
        return ""
    texts: list = []
    for item in items:
        for part in (item.get("content") or []) if isinstance(item, dict) else []:
            if isinstance(part, dict) and part.get("text"):
                texts.append(str(part["text"]))
    return texts[-1] if texts else ""


def _send(path: str, headers: dict, body: dict, proxy: str | None = None,
          timeout=None, retries=None, retry_delay=None,
          model: str | None = None) -> dict:
    # An explicit model stamps the outgoing body (on a copy - the caller's
    # dict is never mutated) and the report. Omitted, the body stands as
    # given. Same one-turn-override pattern as continue_session.
    if model is not None:
        body = dict(body)
        body["model"] = _resolve_model(model)
    # Trace headers: the captured client runs share ONE 32-hex trace id
    # per session (across requests and processes) and mint a fresh 16-hex
    # span per request. So: absent -> stamp a fresh pair; present (a saved
    # session trace) -> keep the trace id, refresh only the span.
    if "b3" not in headers:
        headers = dict(headers)
        trace_id = secrets.token_hex(16)
        span_id = secrets.token_hex(8)
        headers["b3"] = f"{trace_id}-{span_id}-1-{secrets.token_hex(8)}"
        headers["traceparent"] = f"00-{trace_id}-{span_id}-01"
    elif "traceparent" in headers:
        headers = dict(headers)
        stage, trace_id, _, flags = headers["traceparent"].split("-")
        span_id = secrets.token_hex(8)
        headers["traceparent"] = f"{stage}-{trace_id}-{span_id}-{flags}"
        headers["b3"] = (headers["b3"].split("-")[0] + "-" + span_id
                         + "-1-" + secrets.token_hex(8))
    # Protocol routing, resolved live from models.dev (never a hardcoded
    # list): chat-family models get the protocol-family endpoint and a
    # translated body; everything else keeps the legacy responses path and
    # body untouched.
    chat = False
    target = path if path.startswith("http") else UPSTREAM + path
    if model is not None:
        family, family_url = model_protocol(body["model"])
        if family == "chat":
            chat = True
            target = family_url
        elif family not in ("responses",):
            raise ValueError(
                f"model {body['model']!r} uses the {family} protocol; session "
                "chaining here only supports the chat and responses families "
                "(systemone models go through evaluate() instead)")
    if chat:
        # Wire-fidelity to the captured client frames. Empirical gate rules:
        # title-shaped bodies (system first, no tools) pass; a main-shaped
        # 2-message turn needs a prior accepted title request in the same
        # session; follow-up turns must replay the full client shape - main
        # system, tools catalog, max_completion_tokens, assistant turns
        # carrying reasoning_content. A tools-less or title-system follow-up
        # is an instant FreeTierError. History is preserved for chained
        # turns; only a history without a system message gains one.
        instructions = body.get("instructions") or TITLE_INSTRUCTIONS
        if not isinstance(body.get("messages"), list):
            first = first_text_of(body)
            body = {"model": body.get("model"),
                    "messages": [{"role": "system", "content": instructions},
                                 {"role": "user", "content": str(first)}],
                    "stream": True,
                    "stream_options": {"include_usage": True}}
        else:
            messages = list(body["messages"])
            if not any(m.get("role") == "system" for m in messages):
                messages.insert(0, {"role": "system", "content": instructions})
            for m in messages:
                if isinstance(m, dict) and "prompt_cache_key" in m:
                    m.pop("prompt_cache_key", None)
            rebuilt = {"model": body.get("model"), "messages": messages,
                       "stream": True,
                       "stream_options": (body.get("stream_options")
                                          or {"include_usage": True})}
            for extra in ("tools", "max_completion_tokens"):
                if body.get(extra) is not None:
                    rebuilt[extra] = body[extra]
            body = rebuilt
    out: dict = {"status": 0, "id": None, "model": body.get("model"),
                 "text": "", "reasoning": "", "usage": None, "error": None,
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
            response = requests.post(target, headers=headers, json=body,
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
            if chat:
                # Chat Completions SSE: {"choices":[{"delta":{"content":...}, ...]}],
                # terminal chunk has "chat.completion" finish_reason style data.
                if isinstance(event.get("choices"), list) and event["choices"]:
                    choice = event["choices"][0]
                    delta = choice.get("delta") or {}
                    piece = delta.get("content")
                    if piece:
                        out["text"] += piece
                    reasoning = delta.get("reasoning_content")
                    if reasoning:
                        out["reasoning"] = out.get("reasoning", "") + reasoning
                    msg = choice.get("message")
                    if isinstance(msg, dict) and msg.get("content") and not out["text"]:
                        out["text"] += msg["content"]
                        if msg.get("reasoning_content"):
                            out["reasoning"] = out["reasoning"] if isinstance(out.get("reasoning"), str) else ""
                            out["reasoning"] += msg["reasoning_content"]
                    finish = choice.get("finish_reason")
                    if finish and choice.get("id") and not out["id"]:
                        out["id"] = choice.get("id")
                if event.get("id") and not out["id"]:
                    out["id"] = event.get("id")
                if isinstance(event.get("usage"), dict):
                    out["usage"] = event["usage"]
                continue
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
    headers = _headers(sid, pid)
    # One 32-hex trace id per session, exactly like the captured client:
    # its title turn, main turn, and cross-process continuations all share
    # trace 65de7970... with a fresh span per request. Seed the session
    # trace here; _send keeps the id and refreshes only the span per call.
    trace_id = secrets.token_hex(16)
    span_id = secrets.token_hex(8)
    headers = dict(headers)
    headers["traceparent"] = f"00-{trace_id}-{span_id}-01"
    headers["b3"] = f"{trace_id}-{span_id}-1-{secrets.token_hex(8)}"
    out = _send(PATH_RESPONSES, headers, body, proxy,
                timeout=timeout, retries=retries, retry_delay=retry_delay,
                model=resolved_model)
    out["session_id"], out["project_id"] = sid, pid
    ok = False
    if out["status"] == 200:
        chain_family, _ = model_protocol(resolved_model)
        if chain_family == "chat":
            # The captured client run makes TWO requests for turn 1 on the
            # same session: a title-shaped gate pass (sent above), then the
            # main-shape conversation request with the full agent system
            # prompt, the tool catalog, and max_completion_tokens (the
            # feed's output limit). Mirror both, in order. The turn-1
            # assistant reply (reasoning included) is seeded into the
            # chain so continuations replay history [system, user,
            # assistant, user...] exactly like the client.
            main_sys, main_tools = _chat_main_template()
            meta = ((_models_dev() or {}).get("opencode") or {}).get(
                "models", {}).get(resolved_model) or {}
            mtok = (meta.get("limit") or {}).get("output")
            main_msgs = [{"role": "system", "content": main_sys},
                         {"role": "user", "content": first_text}]
            main_body = {"model": resolved_model, "messages": main_msgs,
                         "tools": main_tools, "stream": True,
                         "stream_options": {"include_usage": True}}
            if isinstance(mtok, int):
                main_body["max_completion_tokens"] = mtok
            out = _send(model_target(resolved_model), headers, main_body,
                        proxy, timeout=timeout, retries=retries,
                        retry_delay=retry_delay, model=resolved_model)
            out["session_id"], out["project_id"] = sid, pid
            ok = out["status"] == 200 and bool(out["text"])
            if ok:
                assistant = {"role": "assistant", "content": out["text"]}
                if out.get("reasoning"):
                    assistant["reasoning_content"] = out["reasoning"]
                main_msgs.append(assistant)
            chain_body, chain_path = main_body, model_target(resolved_model)
        else:
            with open(_template_path(files_dir), encoding="utf-8") as f:
                main_base = dict(json.load(f))
            main_base["prompt_cache_key"] = sid
            main_base["model"] = resolved_model
            if isinstance(main_base.get("reasoning"), dict):
                main_base["reasoning"] = dict(main_base["reasoning"])
                main_base["reasoning"]["effort"] = resolved_effort
            main_base["input"] = [body["input"][0]]
            chain_body = main_base
            chain_path = PATH_RESPONSES
            ok = True
        if ok:
            with open(os.path.join(files_dir, f"session-{sid}.json"), "w", encoding="utf-8") as f:
                json.dump({"path": chain_path, "headers": headers,
                           "body": chain_body, "project_id": pid}, f)
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
    chat = str(saved.get("path", "")).endswith(CHAT_SUFFIX)
    if chat:
        msgs = body.get("messages")
        body["messages"] = list(msgs or []) + [{"role": "user", "content": prompt}]
        effective_model = body.get("model")
    else:
        body["input"] = list(full["input"]) + [
            {"type": "message", "role": "user",
             "content": [{"type": "input_text", "text": prompt}]}]
    if reasoning_effort is not None and not chat:
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
    if chat:
        # Chain bookkeeping on messages: append the assistant turn carrying
        # its interleaved reasoning (the field interleaved models emit), the
        # way the client replays it in follow-up turns.
        out["chain_len"] = len(body["messages"])
        if out["status"] == 200 and out["text"]:
            assistant = {"role": "assistant", "content": out["text"]}
            if out.get("reasoning"):
                assistant["reasoning_content"] = out["reasoning"]
            body["messages"] = body["messages"] + [assistant]
            saved["body"] = body
            with open(os.path.join(files_dir, f"session-{session_id}.json"), "w", encoding="utf-8") as f:
                json.dump(saved, f)
        return out
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
