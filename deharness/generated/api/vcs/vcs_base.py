from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.vcs_base_location_type_0 import VcsBaseLocationType0
from ...models.vcs_base_response_200 import VcsBaseResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    location: None | Unset | VcsBaseLocationType0 = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, VcsBaseLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/vcs/base",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200 | None:
    if response.status_code == 200:
        response_200 = VcsBaseResponse200.from_dict(response.json())



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

    if response.status_code == 503:
        response_503 = ServiceUnavailableErrorEncoded.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsBaseLocationType0 = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200]:
    """ VCS review base

     Infer a local review base from named branch creation history, or the repository default only when
    currently on that branch. Returns null before the first commit or when the provider lacks base
    metadata; ambiguous Git history requires an explicit base on diff requests.

    Args:
        location (None | Unset | VcsBaseLocationType0):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200]
     """


    kwargs = _get_kwargs(
        location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsBaseLocationType0 = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200 | None:
    """ VCS review base

     Infer a local review base from named branch creation history, or the repository default only when
    currently on that branch. Returns null before the first commit or when the provider lacks base
    metadata; ambiguous Git history requires an explicit base on diff requests.

    Args:
        location (None | Unset | VcsBaseLocationType0):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200
     """


    return sync_detailed(
        client=client,
location=location,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsBaseLocationType0 = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200]:
    """ VCS review base

     Infer a local review base from named branch creation history, or the repository default only when
    currently on that branch. Returns null before the first commit or when the provider lacks base
    metadata; ambiguous Git history requires an explicit base on diff requests.

    Args:
        location (None | Unset | VcsBaseLocationType0):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200]
     """


    kwargs = _get_kwargs(
        location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsBaseLocationType0 = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200 | None:
    """ VCS review base

     Infer a local review base from named branch creation history, or the repository default only when
    currently on that branch. Returns null before the first commit or when the provider lacks base
    metadata; ambiguous Git history requires an explicit base on diff requests.

    Args:
        location (None | Unset | VcsBaseLocationType0):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsBaseResponse200
     """


    return (await asyncio_detailed(
        client=client,
location=location,

    )).parsed
