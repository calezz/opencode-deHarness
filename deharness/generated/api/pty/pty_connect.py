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
from ...models.pty_not_found_error_encoded import PtyNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    pty_id: str,
    *,
    locationdirectory: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ticket: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["location[directory]"] = locationdirectory

    params["cursor"] = cursor

    params["ticket"] = ticket


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/pty/{pty_id}/connect".format(pty_id=quote(str(pty_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool | None:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool]:
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
    locationdirectory: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ticket: str | Unset = UNSET,

) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool]:
    """ Connect to PTY session

     Establish a WebSocket connection streaming PTY output and accepting terminal input.

    Args:
        pty_id (str):
        locationdirectory (str | Unset):
        cursor (str | Unset):
        ticket (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
locationdirectory=locationdirectory,
cursor=cursor,
ticket=ticket,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    locationdirectory: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ticket: str | Unset = UNSET,

) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool | None:
    """ Connect to PTY session

     Establish a WebSocket connection streaming PTY output and accepting terminal input.

    Args:
        pty_id (str):
        locationdirectory (str | Unset):
        cursor (str | Unset):
        ticket (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool
     """


    return sync_detailed(
        pty_id=pty_id,
client=client,
locationdirectory=locationdirectory,
cursor=cursor,
ticket=ticket,

    ).parsed

async def asyncio_detailed(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    locationdirectory: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ticket: str | Unset = UNSET,

) -> Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool]:
    """ Connect to PTY session

     Establish a WebSocket connection streaming PTY output and accepting terminal input.

    Args:
        pty_id (str):
        locationdirectory (str | Unset):
        cursor (str | Unset):
        ticket (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
locationdirectory=locationdirectory,
cursor=cursor,
ticket=ticket,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    locationdirectory: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    ticket: str | Unset = UNSET,

) -> ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool | None:
    """ Connect to PTY session

     Establish a WebSocket connection streaming PTY output and accepting terminal input.

    Args:
        pty_id (str):
        locationdirectory (str | Unset):
        cursor (str | Unset):
        ticket (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForbiddenErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | bool
     """


    return (await asyncio_detailed(
        pty_id=pty_id,
client=client,
locationdirectory=locationdirectory,
cursor=cursor,
ticket=ticket,

    )).parsed
