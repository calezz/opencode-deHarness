"""Part 1: OpenCode deHarness.

Forms requests exactly as the opencode desktop client does - client-format
session ids, full body shape, chain files - so Python code can drive the
opencode provider with no desktop client, API key, or login.

Contract (Form, never Find): everything needed to form and fire a request,
including through one specific proxy you hand it. No discovery, no scoring,
no pool, no switching proxies. Standalone: imports nothing but stdlib +
`requests` (verified by grep + blocked-import test - see SPEC).

    from deharness import mint_session, continue_session
"""
from deharness.request import (
    CLIENT_VERSION,
    EVAL_TIMEOUT,
    ID_CHARS,
    MODEL,
    MODELS_TIMEOUT,
    PATH_MODELS,
    PATH_RESPONSES,
    PATH_SYSTEMONE,
    REASONING_EFFORT,
    RETRIES,
    RETRY_DELAY,
    TIMEOUT,
    TITLE_INSTRUCTIONS,
    UPSTREAM,
    _headers,
    _proxy_url,
    _send,
    _via,
    continue_session,
    evaluate,
    list_models,
    mint_session,
    mint_session_id,
)

__all__ = [
    "CLIENT_VERSION",
    "EVAL_TIMEOUT",
    "ID_CHARS",
    "MODEL",
    "MODELS_TIMEOUT",
    "PATH_MODELS",
    "PATH_RESPONSES",
    "PATH_SYSTEMONE",
    "REASONING_EFFORT",
    "RETRIES",
    "RETRY_DELAY",
    "TIMEOUT",
    "TITLE_INSTRUCTIONS",
    "UPSTREAM",
    "continue_session",
    "evaluate",
    "list_models",
    "mint_session",
    "mint_session_id",
]
