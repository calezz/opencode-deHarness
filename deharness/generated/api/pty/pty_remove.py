from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.pty_not_found_error_encoded import PtyNotFoundErrorEncoded
from ...models.pty_remove_location_type_0 import PtyRemoveLocationType0
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    pty_id: str,
    *,
    location: None | PtyRemoveLocationType0 | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, PtyRemoveLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/pty/{pty_id}".format(pty_id=quote(str(pty_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
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
    location: None | PtyRemoveLocationType0 | Unset = UNSET,

) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Remove PTY session

     Terminate and remove one PTY session.

    Args:
        pty_id (str):
        location (None | PtyRemoveLocationType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: None | PtyRemoveLocationType0 | Unset = UNSET,

) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Remove PTY session

     Terminate and remove one PTY session.

    Args:
        pty_id (str):
        location (None | PtyRemoveLocationType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        pty_id=pty_id,
client=client,
location=location,

    ).parsed

async def asyncio_detailed(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: None | PtyRemoveLocationType0 | Unset = UNSET,

) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Remove PTY session

     Terminate and remove one PTY session.

    Args:
        pty_id (str):
        location (None | PtyRemoveLocationType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: None | PtyRemoveLocationType0 | Unset = UNSET,

) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Remove PTY session

     Terminate and remove one PTY session.

    Args:
        pty_id (str):
        location (None | PtyRemoveLocationType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        pty_id=pty_id,
client=client,
location=location,

    )).parsed
