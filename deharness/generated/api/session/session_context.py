from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.session_context_response_200 import SessionContextResponse200
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.unknown_error_encoded import UnknownErrorEncoded
from typing import cast



def _get_kwargs(
    session_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/{session_id}/context".format(session_id=quote(str(session_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SessionContextResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = SessionNotFoundErrorEncoded.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = UnknownErrorEncoded.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
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

) -> Response[InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Get session context

     Retrieve the active context messages for a session (all messages after the last compaction).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Get session context

     Retrieve the active context messages for a session (all messages after the last compaction).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Get session context

     Retrieve the active context messages for a session (all messages after the last compaction).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Get session context

     Retrieve the active context messages for a session (all messages after the last compaction).

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | SessionContextResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,

    )).parsed
