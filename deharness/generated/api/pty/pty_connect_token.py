from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.forbidden_error_encoded import ForbiddenErrorEncoded
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.pty_connect_token_location_type_0 import PtyConnectTokenLocationType0
from ...models.pty_connect_token_response_200 import PtyConnectTokenResponse200
from ...models.pty_not_found_error_encoded import PtyNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    pty_id: str,
    *,
    location: None | PtyConnectTokenLocationType0 | Unset = UNSET,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_opencode_ticket, Unset):
        headers["x-opencode-ticket"] = x_opencode_ticket



    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, PtyConnectTokenLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/pty/{pty_id}/connect-token".format(pty_id=quote(str(pty_id), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = PtyConnectTokenResponse200.from_dict(response.json())



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
        def _parse_response_404(data: object) -> LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = PtyNotFoundErrorEncoded.from_dict(data)



                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = LocationNotFoundErrorEncoded.from_dict(data)



            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded]:
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
    location: None | PtyConnectTokenLocationType0 | Unset = UNSET,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded]:
    """ Create PTY WebSocket token

     Create a short-lived single-use ticket for opening a PTY WebSocket connection.

    Args:
        pty_id (str):
        location (None | PtyConnectTokenLocationType0 | Unset):
        x_opencode_ticket (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
location=location,
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
    location: None | PtyConnectTokenLocationType0 | Unset = UNSET,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded | None:
    """ Create PTY WebSocket token

     Create a short-lived single-use ticket for opening a PTY WebSocket connection.

    Args:
        pty_id (str):
        location (None | PtyConnectTokenLocationType0 | Unset):
        x_opencode_ticket (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        pty_id=pty_id,
client=client,
location=location,
x_opencode_ticket=x_opencode_ticket,

    ).parsed

async def asyncio_detailed(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: None | PtyConnectTokenLocationType0 | Unset = UNSET,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded]:
    """ Create PTY WebSocket token

     Create a short-lived single-use ticket for opening a PTY WebSocket connection.

    Args:
        pty_id (str):
        location (None | PtyConnectTokenLocationType0 | Unset):
        x_opencode_ticket (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
location=location,
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
    location: None | PtyConnectTokenLocationType0 | Unset = UNSET,
    x_opencode_ticket: None | str | Unset = UNSET,

) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded | None:
    """ Create PTY WebSocket token

     Create a short-lived single-use ticket for opening a PTY WebSocket connection.

    Args:
        pty_id (str):
        location (None | PtyConnectTokenLocationType0 | Unset):
        x_opencode_ticket (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyConnectTokenResponse200 | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        pty_id=pty_id,
client=client,
location=location,
x_opencode_ticket=x_opencode_ticket,

    )).parsed
