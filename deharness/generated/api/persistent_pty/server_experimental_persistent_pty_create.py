from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.persistent_pty_create_input import PersistentPtyCreateInput
from ...models.server_experimental_persistent_pty_create_response_200 import ServerExperimentalPersistentPtyCreateResponse200
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    body: PersistentPtyCreateInput,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/experimental/session/{session_id}/terminal".format(session_id=quote(str(session_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = ServerExperimentalPersistentPtyCreateResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
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
    body: PersistentPtyCreateInput,

) -> Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ 
    Args:
        session_id (str):
        body (PersistentPtyCreateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
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
    body: PersistentPtyCreateInput,

) -> InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ 
    Args:
        session_id (str):
        body (PersistentPtyCreateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
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
    body: PersistentPtyCreateInput,

) -> Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ 
    Args:
        session_id (str):
        body (PersistentPtyCreateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
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
    body: PersistentPtyCreateInput,

) -> InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ 
    Args:
        session_id (str):
        body (PersistentPtyCreateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | ServerExperimentalPersistentPtyCreateResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
body=body,

    )).parsed
