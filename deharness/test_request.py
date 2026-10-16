"""Offline tests for the deharness (no network, no quota).

Run from the repo root:  python deharness/test_request.py
Covers: body forming (model/instructions/effort/timeout wiring), retry
counts, delay honored, 429-never-retried, chain effort inheritance +
override, old-chain fallback, cwd-default sessions, validation errors,
standalone (no pool refs).
"""
import json
import os
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import deharness as dh
from deharness import request as R

PASS = []


def check(name, cond):
    assert cond, f"FAILED: {name}"
    PASS.append(name)
    print(f"  ok: {name}")


class FakeStream:
    """Minimal requests.Response stand-in for a completed SSE turn."""

    def __init__(self, status=200, events=None, text=""):
        self.status_code = status
        self._events = events or []
        self.text = text

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def iter_lines(self, decode_unicode=True):
        return iter(self._events)


COMPLETED = [
    'data: {"type": "response.created", "response": {"id": "resp_1"}}',
    'data: {"type": "response.output_text.delta", "delta": "OK"}',
    'data: {"type": "response.completed", "response": {"id": "resp_1", '
    '"model": "m", "usage": {}, "output": []}}',
]


class Rig:
    """Patchable transport + clock for request.py."""

    def __init__(self, script):
        # script: list of ("fail", exc) | ("ok", FakeStream) | ("status", code, text)
        self.script = list(script)
        self.calls = []
        self.sleeps = []
        self._real_post = R.requests.post
        self._real_sleep = R.time.sleep

    def __enter__(self):
        def fake_post(url, headers=None, json=None, timeout=None, stream=None, proxies=None):
            self.calls.append({"url": url, "timeout": timeout, "proxies": proxies,
                               "model": (json or {}).get("model"),
                               "effort": ((json or {}).get("reasoning") or {}).get("effort"),
                               "instructions": (json or {}).get("instructions")})
            kind = self.script.pop(0) if self.script else ("ok", FakeStream(events=COMPLETED))
            if kind[0] == "fail":
                raise kind[1]
            if kind[0] == "status":
                return FakeStream(status=kind[1], text=kind[2])
            return kind[1]

        def fake_sleep(s):
            self.sleeps.append(s)

        R.requests.post = fake_post
        R.time.sleep = fake_sleep
        return self

    def __exit__(self, *a):
        R.requests.post = self._real_post
        R.time.sleep = self._real_sleep
        return False


def t_body_forming():
    with Rig([("ok", FakeStream(events=COMPLETED))]) as rig:
        out = R._send("/inference/v1/responses", {"H": "1"},
                      {"model": "m", "input": []},
                      timeout=11, retries=0, retry_delay=0)
    check("200 completes", out["status"] == 200 and out["text"] == "OK")
    check("timeout passed", rig.calls[0]["timeout"] == 11)
    check("model passed", rig.calls[0]["model"] == "m")


def t_retry_counts():
    with Rig([("fail", ConnectionError("down"))] * 5) as rig:
        out = R._send("/x", {}, {"model": "m"}, retries=2, retry_delay=0)
    check("retries=2 -> 3 attempts", len(rig.calls) == 3)
    check("error surfaces", out["status"] == 0 and "down" in out["error"])
    with Rig([("fail", TimeoutError("t"))] * 5) as rig:
        R._send("/x", {}, {"model": "m"}, retries=0, retry_delay=0)
    check("retries=0 -> 1 attempt", len(rig.calls) == 1)


def t_retry_then_success_and_delay():
    with Rig([("fail", ConnectionError("a")), ("fail", ConnectionError("b")),
              ("ok", FakeStream(events=COMPLETED))]) as rig:
        out = R._send("/x", {}, {"model": "m"}, retries=5, retry_delay=5)
    check("succeeds on 3rd try", out["status"] == 200)
    check("delay honored twice", rig.sleeps == [5, 5])


def t_status_never_retried():
    with Rig([("status", 429, "FreeUsageLimitError")]) as rig:
        out = R._send("/x", {}, {"model": "m"}, retries=5, retry_delay=0)
    check("429 returned, not retried", out["status"] == 429 and len(rig.calls) == 1)


def t_send_model_override():
    with Rig([("ok", FakeStream(events=COMPLETED))]) as rig:
        out = R._send("/x", {}, {"model": "old"}, model="new",
                      retries=0, retry_delay=0)
    check("override stamps sent body", rig.calls[0]["model"] == "new")
    check("server-echoed model wins the report", out["model"] == "m")
    mine = {"model": "old"}
    with Rig([("ok", FakeStream(events=COMPLETED))]):
        R._send("/x", {}, mine, model="new", retries=0, retry_delay=0)
    check("caller body not mutated", mine == {"model": "old"})
    bare = [e for e in COMPLETED if "response.completed" not in e]
    with Rig([("ok", FakeStream(events=bare))]) as rig:
        out = R._send("/x", {}, {"model": "old"}, model="new",
                      retries=0, retry_delay=0)
    check("no server echo -> report keeps override", out["model"] == "new")
    with Rig([("ok", FakeStream(events=COMPLETED))]) as rig:
        out = R._send("/x", {}, {"model": "kept"}, retries=0, retry_delay=0)
    check("omitted model leaves body standing",
          rig.calls[0]["model"] == "kept" and out["model"] == "m")
    try:
        R._send("/x", {}, {"model": "m"}, model="  ", retries=0, retry_delay=0)
        raise AssertionError("no ValueError")
    except ValueError:
        pass
    check("empty override raises ValueError", True)


def t_validation():
    for kw in ({"retries": -1}, {"timeout": 0}, {"retry_delay": -1},
               {"timeout": "soon"}):
        try:
            R._send("/x", {}, {"model": "m"}, **kw)
            raise AssertionError(f"no ValueError for {kw}")
        except ValueError:
            pass
    try:
        dh.mint_session("hi", model="  ", files_dir=tempfile.mkdtemp(),
                        retries=0, retry_delay=0)
        raise AssertionError("no ValueError for empty model")
    except ValueError:
        pass
    try:
        dh.mint_session("hi", reasoning_effort="", files_dir=tempfile.mkdtemp(),
                        retries=0, retry_delay=0)
        raise AssertionError("no ValueError for empty effort")
    except ValueError:
        pass
    check("bad model/timeout/retries/delay raise ValueError", True)


def t_mint_chain_roundtrip():
    import shutil
    d = tempfile.mkdtemp(prefix="deharness-test-")
    shutil.copy(os.path.join(os.path.dirname(R.__file__),
                             "template-main-body.json"), d)
    with Rig([("ok", FakeStream(events=COMPLETED))]):
        out = dh.mint_session("hi", model="test-model", reasoning_effort="low",
                              files_dir=d, retries=0, retry_delay=0,
                              instructions="CUSTOM-INSTR")
    check("mint 200", out["status"] == 200)
    with open(os.path.join(d, f"session-{out['session_id']}.json")) as f:
        saved = json.load(f)
    check("chain stores model", saved["body"]["model"] == "test-model")
    check("chain stores effort", saved["body"]["reasoning"]["effort"] == "low")
    check("chain stores prompt key", saved["body"]["prompt_cache_key"] == out["session_id"])
    with Rig([("ok", FakeStream(events=COMPLETED))]) as rig:
        r2 = dh.continue_session("again?", out["session_id"], files_dir=d,
                                 retries=0, retry_delay=0)
    check("continue 200", r2["status"] == 200)
    check("continue inherits effort", rig.calls[0]["effort"] == "low")
    check("continue inherits model", rig.calls[0]["model"] == "test-model")
    with Rig([("ok", FakeStream(events=COMPLETED))]) as rig:
        dh.continue_session("harder?", out["session_id"], files_dir=d,
                            reasoning_effort="xhigh", retries=0, retry_delay=0)
    check("override applies one turn", rig.calls[0]["effort"] == "xhigh")
    with open(os.path.join(d, f"session-{out['session_id']}.json")) as f:
        saved2 = json.load(f)
    check("override not persisted", saved2["body"]["reasoning"]["effort"] == "low")


def t_old_chain_fallback():
    d = tempfile.mkdtemp(prefix="deharness-test-")
    sid = dh.mint_session_id()
    legacy = {"path": "/inference/v1/responses",
              "headers": {"H": "1"},
              "body": {"input": [], "prompt_cache_key": sid},
              "project_id": "p"}
    with open(os.path.join(d, f"session-{sid}.json"), "w") as f:
        json.dump(legacy, f)
    with Rig([("ok", FakeStream(events=COMPLETED))]) as rig:
        out = dh.continue_session("hi?", sid, files_dir=d, retries=0, retry_delay=0)
    check("old chain (no model/effort keys) still works", out["status"] == 200)
    check("old chain posts module default timeout",
          rig.calls[0]["timeout"] == dh.TIMEOUT)


def t_cwd_default():
    d = tempfile.mkdtemp(prefix="deharness-test-")
    prev = os.getcwd()
    os.chdir(d)
    try:
        with Rig([("ok", FakeStream(events=COMPLETED))]):
            out = dh.mint_session("hi", retries=0, retry_delay=0)
        check("default files_dir mints 200", out["status"] == 200)
        here = os.path.join(d, f"session-{out['session_id']}.json")
        check("chain lands in cwd, not the package",
              os.path.exists(here) and not os.path.exists(
                  os.path.join(os.path.dirname(R.__file__),
                               f"session-{out['session_id']}.json")))
    finally:
        os.chdir(prev)


def t_protocol_marker():
    body = ('{"type":"error","error":{"type":"ModelProtocolUnsupported",'
            '"message":"Model does not support this protocol."}}')
    with Rig([("status", 400, body)]) as rig:
        out = R._send("/x", {}, {"model": "m"}, retries=0, retry_delay=0)
    check("protocol failure marked", out.get("error_kind") == "model-protocol-unsupported")
    check("protocol failure not retried", len(rig.calls) == 1)
    with Rig([("status", 429, "FreeUsageLimitError")]) as rig:
        out = R._send("/x", {}, {"model": "m"}, retries=0, retry_delay=0)
    check("other errors carry no marker", "error_kind" not in out)


def t_standalone():
    import subprocess
    # No path hacks: deharness must resolve from the INSTALLED package
    # (pip install -e), proving the shipped artifact is standalone.
    # cwd is a bare temp dir so the source tree cannot satisfy the import.
    code = ("import builtins; _r=builtins.__import__;"
            "builtins.__import__=lambda n,*a,**k: (_ for _ in ()).throw(ImportError('blocked')) "
            "if n=='proxy_pool' or n.startswith('proxy_pool.') else _r(n,*a,**k);"
            "import deharness; s=deharness.mint_session_id();"
            "print('standalone-import-ok', s[:8], deharness.__file__)")
    r = subprocess.run([sys.executable, "-c", code], capture_output=True,
                       text=True, timeout=60,
                       cwd=tempfile.mkdtemp(prefix="deharness-standalone-"))
    check("installed deharness imports with pool blocked",
          "standalone-import-ok" in r.stdout)


if __name__ == "__main__":
    print("deharness offline tests (no network):")
    t_body_forming()
    t_retry_counts()
    t_retry_then_success_and_delay()
    t_status_never_retried()
    t_send_model_override()
    t_validation()
    t_mint_chain_roundtrip()
    t_old_chain_fallback()
    t_cwd_default()
    t_protocol_marker()
    t_standalone()
    print(f"\nALL {len(PASS)} DEHARNESS TESTS PASSED")
