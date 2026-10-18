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
from ...models.pty_update_body import PtyUpdateBody
from ...models.pty_update_location_type_0 import PtyUpdateLocationType0
from ...models.pty_update_response_200 import PtyUpdateResponse200
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    pty_id: str,
    *,
    body: PtyUpdateBody,
    location: None | PtyUpdateLocationType0 | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, PtyUpdateLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/pty/{pty_id}".format(pty_id=quote(str(pty_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = PtyUpdateResponse200.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded]:
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
    body: PtyUpdateBody,
    location: None | PtyUpdateLocationType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded]:
    """ Update PTY session

     Update the title or viewport size of one PTY session.

    Args:
        pty_id (str):
        location (None | PtyUpdateLocationType0 | Unset):
        body (PtyUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
body=body,
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
    body: PtyUpdateBody,
    location: None | PtyUpdateLocationType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded | None:
    """ Update PTY session

     Update the title or viewport size of one PTY session.

    Args:
        pty_id (str):
        location (None | PtyUpdateLocationType0 | Unset):
        body (PtyUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        pty_id=pty_id,
client=client,
body=body,
location=location,

    ).parsed

async def asyncio_detailed(
    pty_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PtyUpdateBody,
    location: None | PtyUpdateLocationType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded]:
    """ Update PTY session

     Update the title or viewport size of one PTY session.

    Args:
        pty_id (str):
        location (None | PtyUpdateLocationType0 | Unset):
        body (PtyUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        pty_id=pty_id,
body=body,
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
    body: PtyUpdateBody,
    location: None | PtyUpdateLocationType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded | None:
    """ Update PTY session

     Update the title or viewport size of one PTY session.

    Args:
        pty_id (str):
        location (None | PtyUpdateLocationType0 | Unset):
        body (PtyUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | PtyNotFoundErrorEncoded | PtyUpdateResponse200 | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        pty_id=pty_id,
client=client,
body=body,
location=location,

    )).parsed
