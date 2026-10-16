"""Example 3: list all live models (no auth needed)."""
from deharness import list_models

for mid in list_models():
    print(mid)
