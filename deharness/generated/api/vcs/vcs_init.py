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
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.vcs_init_location_type_0 import VcsInitLocationType0
from ...models.vcs_init_not_supported_error_encoded import VcsInitNotSupportedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    location: None | Unset | VcsInitLocationType0 = UNSET,
    provider: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, VcsInitLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location

    json_provider: None | str | Unset
    if isinstance(provider, Unset):
        json_provider = UNSET
    else:
        json_provider = provider
    params["provider"] = json_provider


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/vcs/init",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded | None:
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
        response_404 = LocationNotFoundErrorEncoded.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = ConflictErrorEncoded.from_dict(response.json())



        return response_409

    if response.status_code == 501:
        response_501 = VcsInitNotSupportedErrorEncoded.from_dict(response.json())



        return response_501

    if response.status_code == 503:
        response_503 = ServiceUnavailableErrorEncoded.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsInitLocationType0 = UNSET,
    provider: None | str | Unset = UNSET,

) -> Response[Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded]:
    """ Initialize VCS repository

     Initialize a repository using the selected VCS provider in a markerless project's directory and
    refresh its location services. Omitting provider defaults to git; built-in git and hg providers
    support initialization. An unknown provider returns 400; a registered provider without init returns
    501.

    Args:
        location (None | Unset | VcsInitLocationType0):
        provider (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded]
     """


    kwargs = _get_kwargs(
        location=location,
provider=provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsInitLocationType0 = UNSET,
    provider: None | str | Unset = UNSET,

) -> Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded | None:
    """ Initialize VCS repository

     Initialize a repository using the selected VCS provider in a markerless project's directory and
    refresh its location services. Omitting provider defaults to git; built-in git and hg providers
    support initialization. An unknown provider returns 400; a registered provider without init returns
    501.

    Args:
        location (None | Unset | VcsInitLocationType0):
        provider (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded
     """


    return sync_detailed(
        client=client,
location=location,
provider=provider,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsInitLocationType0 = UNSET,
    provider: None | str | Unset = UNSET,

) -> Response[Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded]:
    """ Initialize VCS repository

     Initialize a repository using the selected VCS provider in a markerless project's directory and
    refresh its location services. Omitting provider defaults to git; built-in git and hg providers
    support initialization. An unknown provider returns 400; a registered provider without init returns
    501.

    Args:
        location (None | Unset | VcsInitLocationType0):
        provider (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded]
     """


    kwargs = _get_kwargs(
        location=location,
provider=provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsInitLocationType0 = UNSET,
    provider: None | str | Unset = UNSET,

) -> Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded | None:
    """ Initialize VCS repository

     Initialize a repository using the selected VCS provider in a markerless project's directory and
    refresh its location services. Omitting provider defaults to git; built-in git and hg providers
    support initialization. An unknown provider returns 400; a registered provider without init returns
    501.

    Args:
        location (None | Unset | VcsInitLocationType0):
        provider (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConflictErrorEncoded | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsInitNotSupportedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
location=location,
provider=provider,

    )).parsed
