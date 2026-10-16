"""Example 2: chained conversation with memory on a minted session."""
from deharness import continue_session, mint_session

sid = mint_session("hello")["session_id"]

r1 = continue_session("remember the codeword JUNIPER. reply exactly: stored",
                      session_id=sid)
print("turn 1:", r1["status"], repr(r1["text"]), "chain:", r1["chain_len"])

r2 = continue_session("what is the codeword? reply with only that word",
                      session_id=sid)
print("turn 2:", r2["status"], repr(r2["text"]), "chain:", r2["chain_len"])
assert r2["text"].strip() == "JUNIPER"
