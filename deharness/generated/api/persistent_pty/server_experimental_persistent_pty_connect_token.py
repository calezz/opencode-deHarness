from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.forbidden_error_encoded import ForbiddenErrorEncoded
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.pty_not_found_error_encoded import PtyNotFoundErrorEncoded
from ...models.server_experimental_persistent_pty_connect_token_response_200 import ServerExperimentalPersistentPtyConnectTokenResponse200
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    pty_id: str,
    *,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_opencode_ticket, Unset):
        headers["x-opencode-ticket"] = x_opencode_ticket



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/experimental/persistent-pty/{pty_id}/connect-token".format(pty_id=quote(str(pty_id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = ServerExperimentalPersistentPtyConnectTokenResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ForbiddenErrorEncoded.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PtyNotFoundErrorEncoded.from_dict(response.json())



        return response_404

    if response.status_code == 503:
        response_503 = ServiceUnavailableErrorEncoded.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ 
    Args:
        pty_id (str):
        x_opencode_ticket (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
x_opencode_ticket=x_opencode_ticket,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ 
    Args:
        pty_id (str):
        x_opencode_ticket (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        pty_id=pty_id,
client=client,
x_opencode_ticket=x_opencode_ticket,

    ).parsed

async def asyncio_detailed(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ 
    Args:
        pty_id (str):
        x_opencode_ticket (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
x_opencode_ticket=x_opencode_ticket,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ 
    Args:
        pty_id (str):
        x_opencode_ticket (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForbiddenErrorEncoded | InvalidRequestErrorEncoded | PtyNotFoundErrorEncoded | ServerExperimentalPersistentPtyConnectTokenResponse200 | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        pty_id=pty_id,
client=client,
x_opencode_ticket=x_opencode_ticket,

    )).parsed
