from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.plugin_update_body import PluginUpdateBody
from ...models.plugin_update_location_type_0 import PluginUpdateLocationType0
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: PluginUpdateBody,
    location: None | PluginUpdateLocationType0 | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, PluginUpdateLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/plugin/update",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
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

    if response.status_code == 503:
        response_503 = ServiceUnavailableErrorEncoded.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PluginUpdateBody,
    location: None | PluginUpdateLocationType0 | Unset = UNSET,

) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ Update plugins

     Update package plugins concurrently and notify active locations to reload them. Responds once every
    update has finished; fails when any update fails.

    Args:
        location (None | PluginUpdateLocationType0 | Unset):
        body (PluginUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        body=body,
location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PluginUpdateBody,
    location: None | PluginUpdateLocationType0 | Unset = UNSET,

) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Update plugins

     Update package plugins concurrently and notify active locations to reload them. Responds once every
    update has finished; fails when any update fails.

    Args:
        location (None | PluginUpdateLocationType0 | Unset):
        body (PluginUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,
body=body,
location=location,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PluginUpdateBody,
    location: None | PluginUpdateLocationType0 | Unset = UNSET,

) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ Update plugins

     Update package plugins concurrently and notify active locations to reload them. Responds once every
    update has finished; fails when any update fails.

    Args:
        location (None | PluginUpdateLocationType0 | Unset):
        body (PluginUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        body=body,
location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PluginUpdateBody,
    location: None | PluginUpdateLocationType0 | Unset = UNSET,

) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Update plugins

     Update package plugins concurrently and notify active locations to reload them. Responds once every
    update has finished; fails when any update fails.

    Args:
        location (None | PluginUpdateLocationType0 | Unset):
        body (PluginUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
body=body,
location=location,

    )).parsed
