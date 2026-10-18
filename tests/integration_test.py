#!/usr/bin/env python3
"""
Integration test: mint a session and continue it on a free model.
Must pass for CI to accept generated client updates.
"""
import os
import sys
import tempfile
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from deharness.request import mint_session, continue_session


def test_mint_and_continue():
    with tempfile.TemporaryDirectory() as tmpdir:
        files_dir = os.path.join(tmpdir, "sessions")
        os.makedirs(files_dir, exist_ok=True)

        # Mint a session with beam-free (free model)
        print("Minting session...")
        m = mint_session(
            "Say exactly: integration test works",
            model="beam-free",
            files_dir=files_dir,
            timeout=120,
        )
        print(f"  mint status: {m['status']}")
        if m["status"] != 200:
            print(f"  MINT FAILED: {m.get('error')}")
            return False
        if "integration test works" not in m["text"].lower():
            print(f"  UNEXPECTED TEXT: {m['text']}")
            return False
        sid = m["session_id"]
        print(f"  session: {sid}")

        # Continue the session
        print("Continuing session...")
        c = continue_session(
            "Say exactly: continuation works",
            sid,
            files_dir=files_dir,
            timeout=120,
        )
        print(f"  continue status: {c['status']}")
        if c["status"] != 200:
            print(f"  CONTINUE FAILED: {c.get('error')}")
            return False
        # Model may return empty for some prompts; accept any 200 with chain extension
        if c["chain_len"] < 4:
            print(f"  CHAIN NOT EXTENDED: chain_len={c['chain_len']}")
            return False
        print(f"  chain_len: {c['chain_len']}, text: {repr(c['text'])[:60]}")

    print("Integration test PASSED")
    return True


if __name__ == "__main__":
    ok = test_mint_and_continue()
    sys.exit(0 if ok else 1)