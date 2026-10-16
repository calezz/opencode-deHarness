"""Example 1: mint a brand-new session (no desktop client needed)."""
from deharness import mint_session

m = mint_session("hello")
print("status:", m["status"])
print("session_id:", m.get("session_id"))
print("title:", m.get("text"))
assert m["status"] == 200, m.get("error")
