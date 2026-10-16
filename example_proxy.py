"""Example 5: route one request through one proxy you already have.

This is deliberately a PLACEHOLDER, not a working proxy: this repo is the
standalone deharness, so nothing here finds proxies for you. Replace
YOUR-PROXY-HERE with a real one (host:port, or a scheme:// URL) and the
same call just works - the deharness routes through whatever it is given.

No pool, no rotation, no scoring: a dead proxy fails fast with its error.
"""
from deharness import mint_session

# vvvv REPLACE THIS WITH YOUR PROXY - this address is documentation-only
# and will not connect to anything. vvvv
PROXY = "YOUR-PROXY-HERE:8080"

m = mint_session("hello", proxy=PROXY, retries=0)
print("status:", m["status"])
print("via:", m.get("via"))
if m["status"] != 200:
    print("error:", (m.get("error") or "")[:200])
    print("(expected until PROXY above is replaced with a real one)")
