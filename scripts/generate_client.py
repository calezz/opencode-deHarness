#!/usr/bin/env python3
"""
Fetch OpenCode OpenAPI spec and generate typed Python client.
Runs in CI; commits generated/ if tests pass.
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
GEN_DIR = ROOT / "deharness" / "generated"
SPEC_URL = "https://opencode.ai/openapi.json"
MODELS_URL = "https://models.dev/api.json"


def fetch_spec(url: str) -> dict:
    import urllib.request
    req = urllib.request.Request(url, headers={"User-Agent": "opencode/latest/2.0.32/desktop"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def write_spec(spec: dict, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(spec, indent=2, sort_keys=True))


def generate_client(spec_path: Path, out_dir: Path):
    """Generate Python client using openapi-python-client."""
    out_dir.mkdir(parents=True, exist_ok=True)
    # Use the modern generator (openapi-python-client >= 0.17)
    cmd = [
        sys.executable, "-m", "openapi_python_client",
        "generate",
        "--path", str(spec_path),
        "--output-path", str(out_dir),
        "--overwrite",
        "--meta", "none",  # don't generate pyproject.toml etc.
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.returncode != 0:
        print("Generation failed:", result.stderr)
        return False
    return True


def patch_generated(gen_dir: Path):
    """Post-process generated code: fix imports, add typing hints."""
    # The generator creates a package structure; we just ensure it's importable
    init_file = gen_dir / "opencode" / "__init__.py"
    if init_file.exists():
        content = init_file.read_text()
        if "from .api" not in content:
            init_file.write_text("from .api import *\n" + content)


def run_tests() -> bool:
    """Run the deharness integration test (mint + continue on beam-free)."""
    test_script = ROOT / "tests" / "integration_test.py"
    if not test_script.exists():
        print("Test script not found:", test_script)
        return False
    result = subprocess.run([sys.executable, str(test_script)], capture_output=True, text=True, cwd=ROOT)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)
    return result.returncode == 0


def main():
    print("Fetching OpenAPI spec...")
    spec = fetch_spec(SPEC_URL)
    spec_path = GEN_DIR / "openapi.json"
    write_spec(spec, spec_path)
    print(f"Spec written to {spec_path}")

    print("Generating client...")
    if not generate_client(spec_path, GEN_DIR):
        sys.exit(1)

    patch_generated(GEN_DIR)
    print("Generation complete.")

    print("Running integration tests...")
    if not run_tests():
        print("Tests failed — not committing generated code.")
        sys.exit(1)

    print("All good. Generated client ready.")


if __name__ == "__main__":
    main()