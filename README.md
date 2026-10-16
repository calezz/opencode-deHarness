# OpenCode deHarness

Use the opencode provider from Python, shaped exactly like the desktop
client. No harness, no login, no API key.

```bash
pip install opencode-deharness
```

```python
from deharness import mint_session, continue_session

m = mint_session("hello")   # -> {"status": 200, "session_id": "ses_...", ...}
r = continue_session("remember JUNIPER", session_id=m["session_id"])
print(r["text"])
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

Full docs: https://github.com/YOU/zen-free
