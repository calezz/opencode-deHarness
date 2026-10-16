# OpenCode deHarness

Use the opencode provider from Python, shaped exactly like the desktop
client. No harness, no login, no API key.

```bash
pip install opencode-deharness
```

```python
from deharness import continue_session, evaluate, list_models, mint_session

# 1. start a session
m = mint_session("hello")   # -> {"status": 200, "session_id": "ses_...", ...}
sid = m["session_id"]

# 2. chain execution: every turn remembers the earlier ones
r1 = continue_session("remember the codeword JUNIPER.", session_id=sid)
r2 = continue_session("what is the codeword?", session_id=sid)
print(r2["text"])       # JUNIPER
print(r2["chain_len"])  # turns stored in session-<ses_...>.json

# 3. ask anything, any turn, with per-turn control
r = continue_session("explain it like I'm five", session_id=sid,
                     model="...", reasoning_effort="xhigh")

# 4. structured questions (answers, no free text)
r = evaluate("jev-1.13-free", state="...",
             questions={"urgent": {"type": "noul", "instructions": "..."}})
print(r["status"], r["answers"])

# 5. list models / route through one proxy you supply
for mid in list_models():   # live catalog, no auth needed
    print(mid)
m = mint_session("hello", proxy="YOUR-PROXY-HERE:8080")
```

### Copy-paste everything

```python
import deharness
from deharness import continue_session, mint_session

# global defaults (change once, applies everywhere None is passed)
deharness.MODEL = "muse-spark-1.3-contributor-free"
deharness.REASONING_EFFORT = "xhigh"
deharness.TIMEOUT = 180
deharness.RETRIES = 2
deharness.RETRY_DELAY = 1.0

m = mint_session(
    "hello",
    model="muse-spark-1.3-contributor-free",
    reasoning_effort="low",
    timeout=180,
    retries=0,
    retry_delay=0,
    proxy=None,          # or "host:port" / "socks5://..." to route it
    instructions=None,   # or your own title prompt
    files_dir=None,      # default: your cwd
)
sid = m["session_id"]

r = continue_session(
    "what is the codeword?",
    session_id=sid,
    model=None,               # None = keep the chain's model
    reasoning_effort="xhigh",  # one turn only, chain unchanged
    timeout=None,
    retries=None,
    retry_delay=None,
    proxy=None,
)
print(r["status"], r["text"])
```

Five runnable scripts live beside this file: `example_mint.py`,
`example_chain.py` (multi-turn memory proof), `example_list.py`,
`example_jev.py` (structured evaluation), `example_proxy.py` (route through
one proxy you supply - it ships with an obvious `YOUR-PROXY-HERE`
placeholder and no proxy-finding of any kind).

Everything formable is settable (module property + per-call kwarg, `None`
means the property): `MODEL`, `TIMEOUT`, `RETRIES`, `RETRY_DELAY`,
`REASONING_EFFORT`. Session files land in your working directory by default
(pass `files_dir=` to put them elsewhere).

Full docs: https://github.com/YOU/opencode-deharness
