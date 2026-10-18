from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conflict_error_encoded import ConflictErrorEncoded
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.session_compact_body import SessionCompactBody
from ...models.session_compact_response_200 import SessionCompactResponse200
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    body: SessionCompactBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/session/{session_id}/compact".format(session_id=quote(str(session_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SessionCompactResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        def _parse_response_404(data: object) -> LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = SessionNotFoundErrorEncoded.from_dict(data)



                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = LocationNotFoundErrorEncoded.from_dict(data)



            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ConflictErrorEncoded.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded]:
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
    body: SessionCompactBody,

) -> Response[ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded]:
    """ Compact session

     Durably admit a session compaction request. Steers by default: it runs at the next step boundary
    instead of waiting behind queued prompts.

    Args:
        session_id (str):
        body (SessionCompactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SessionCompactBody,

) -> ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded | None:
    """ Compact session

     Durably admit a session compaction request. Steers by default: it runs at the next step boundary
    instead of waiting behind queued prompts.

    Args:
        session_id (str):
        body (SessionCompactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SessionCompactBody,

) -> Response[ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded]:
    """ Compact session

     Durably admit a session compaction request. Steers by default: it runs at the next step boundary
    instead of waiting behind queued prompts.

    Args:
        session_id (str):
        body (SessionCompactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SessionCompactBody,

) -> ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded | None:
    """ Compact session

     Durably admit a session compaction request. Steers by default: it runs at the next step boundary
    instead of waiting behind queued prompts.

    Args:
        session_id (str):
        body (SessionCompactBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionCompactResponse200 | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
body=body,

    )).parsed
