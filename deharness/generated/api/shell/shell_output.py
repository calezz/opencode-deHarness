from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.shell_not_found_error_encoded import ShellNotFoundErrorEncoded
from ...models.shell_output_location_type_0 import ShellOutputLocationType0
from ...models.shell_output_response_200 import ShellOutputResponse200
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    location: None | ShellOutputLocationType0 | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, ShellOutputLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/shell/{id}/output".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = ShellOutputResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        def _parse_response_404(data: object) -> LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = ShellNotFoundErrorEncoded.from_dict(data)



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    location: None | ShellOutputLocationType0 | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: str | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded]:
    """ Read shell output

     Page through captured combined output by absolute byte cursor.

    Args:
        id (str):
        location (None | ShellOutputLocationType0 | Unset):
        cursor (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        id=id,
location=location,
cursor=cursor,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    location: None | ShellOutputLocationType0 | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: str | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded | None:
    """ Read shell output

     Page through captured combined output by absolute byte cursor.

    Args:
        id (str):
        location (None | ShellOutputLocationType0 | Unset):
        cursor (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        id=id,
client=client,
location=location,
cursor=cursor,
limit=limit,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    location: None | ShellOutputLocationType0 | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: str | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded]:
    """ Read shell output

     Page through captured combined output by absolute byte cursor.

    Args:
        id (str):
        location (None | ShellOutputLocationType0 | Unset):
        cursor (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        id=id,
location=location,
cursor=cursor,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    location: None | ShellOutputLocationType0 | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: str | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded | None:
    """ Read shell output

     Page through captured combined output by absolute byte cursor.

    Args:
        id (str):
        location (None | ShellOutputLocationType0 | Unset):
        cursor (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ShellNotFoundErrorEncoded | ShellOutputResponse200 | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        id=id,
client=client,
location=location,
cursor=cursor,
limit=limit,

    )).parsed
