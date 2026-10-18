from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.fs_find_location_type_0 import FsFindLocationType0
from ...models.fs_find_response_200 import FsFindResponse200
from ...models.fs_find_type import FsFindType
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    location: FsFindLocationType0 | None | Unset = UNSET,
    query: str,
    type_: FsFindType | Unset = UNSET,
    limit: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, FsFindLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location

    params["query"] = query

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_limit: None | str | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/fs/find",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = FsFindResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = LocationNotFoundErrorEncoded.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: FsFindLocationType0 | None | Unset = UNSET,
    query: str,
    type_: FsFindType | Unset = UNSET,
    limit: None | str | Unset = UNSET,

) -> Response[FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Find files

     Find recursively ranked filesystem entries relative to the requested location.

    Args:
        location (FsFindLocationType0 | None | Unset):
        query (str):
        type_ (FsFindType | Unset):
        limit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        location=location,
query=query,
type_=type_,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    location: FsFindLocationType0 | None | Unset = UNSET,
    query: str,
    type_: FsFindType | Unset = UNSET,
    limit: None | str | Unset = UNSET,

) -> FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Find files

     Find recursively ranked filesystem entries relative to the requested location.

    Args:
        location (FsFindLocationType0 | None | Unset):
        query (str):
        type_ (FsFindType | Unset):
        limit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,
location=location,
query=query,
type_=type_,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: FsFindLocationType0 | None | Unset = UNSET,
    query: str,
    type_: FsFindType | Unset = UNSET,
    limit: None | str | Unset = UNSET,

) -> Response[FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Find files

     Find recursively ranked filesystem entries relative to the requested location.

    Args:
        location (FsFindLocationType0 | None | Unset):
        query (str):
        type_ (FsFindType | Unset):
        limit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        location=location,
query=query,
type_=type_,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    location: FsFindLocationType0 | None | Unset = UNSET,
    query: str,
    type_: FsFindType | Unset = UNSET,
    limit: None | str | Unset = UNSET,

) -> FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Find files

     Find recursively ranked filesystem entries relative to the requested location.

    Args:
        location (FsFindLocationType0 | None | Unset):
        query (str):
        type_ (FsFindType | Unset):
        limit (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FsFindResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
location=location,
query=query,
type_=type_,
limit=limit,

    )).parsed
