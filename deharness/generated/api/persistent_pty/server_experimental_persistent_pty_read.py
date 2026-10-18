from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.server_experimental_persistent_pty_read_response_200 import ServerExperimentalPersistentPtyReadResponse200
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    lines: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_lines: None | str | Unset
    if isinstance(lines, Unset):
        json_lines = UNSET
    else:
        json_lines = lines
    params["lines"] = json_lines


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/experimental/session/{session_id}/terminal/read".format(session_id=quote(str(session_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = ServerExperimentalPersistentPtyReadResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 503:
        response_503 = ServiceUnavailableErrorEncoded.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    lines: None | str | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ Read the session's most recently controlled terminal

     Read the last physical rows without changing selection or taking control. Omitted lines uses the
    live terminal height; larger counts include retained history. Blank rows are preserved. Screen
    dimensions and cursor remain relative to the live screen. Returns null when no current terminal
    exists. Selection is server-local and resets on restart. Experimental: may change without
    compatibility guarantees.

    Args:
        session_id (str):
        lines (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
lines=lines,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    lines: None | str | Unset = UNSET,

) -> InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Read the session's most recently controlled terminal

     Read the last physical rows without changing selection or taking control. Omitted lines uses the
    live terminal height; larger counts include retained history. Blank rows are preserved. Screen
    dimensions and cursor remain relative to the live screen. Returns null when no current terminal
    exists. Selection is server-local and resets on restart. Experimental: may change without
    compatibility guarantees.

    Args:
        session_id (str):
        lines (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,
lines=lines,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    lines: None | str | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ Read the session's most recently controlled terminal

     Read the last physical rows without changing selection or taking control. Omitted lines uses the
    live terminal height; larger counts include retained history. Blank rows are preserved. Screen
    dimensions and cursor remain relative to the live screen. Returns null when no current terminal
    exists. Selection is server-local and resets on restart. Experimental: may change without
    compatibility guarantees.

    Args:
        session_id (str):
        lines (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
lines=lines,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    lines: None | str | Unset = UNSET,

) -> InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Read the session's most recently controlled terminal

     Read the last physical rows without changing selection or taking control. Omitted lines uses the
    live terminal height; larger counts include retained history. Blank rows are preserved. Screen
    dimensions and cursor remain relative to the live screen. Returns null when no current terminal
    exists. Selection is server-local and resets on restart. Experimental: may change without
    compatibility guarantees.

    Args:
        session_id (str):
        lines (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyReadResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
lines=lines,

    )).parsed
