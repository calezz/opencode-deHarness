from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integration_command_cancel_location_type_0 import IntegrationCommandCancelLocationType0
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    integration_id: str,
    attempt_id: str,
    *,
    location: IntegrationCommandCancelLocationType0 | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, IntegrationCommandCancelLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/integration/{integration_id}/connect/command/{attempt_id}".format(integration_id=quote(str(integration_id), safe=""),attempt_id=quote(str(attempt_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_id: str,
    attempt_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: IntegrationCommandCancelLocationType0 | None | Unset = UNSET,

) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Cancel command connection

     Cancel a command authentication attempt and terminate its process.

    Args:
        integration_id (str):
        attempt_id (str):
        location (IntegrationCommandCancelLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        integration_id=integration_id,
attempt_id=attempt_id,
location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    integration_id: str,
    attempt_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: IntegrationCommandCancelLocationType0 | None | Unset = UNSET,

) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Cancel command connection

     Cancel a command authentication attempt and terminate its process.

    Args:
        integration_id (str):
        attempt_id (str):
        location (IntegrationCommandCancelLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        integration_id=integration_id,
attempt_id=attempt_id,
client=client,
location=location,

    ).parsed

async def asyncio_detailed(
    integration_id: str,
    attempt_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: IntegrationCommandCancelLocationType0 | None | Unset = UNSET,

) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Cancel command connection

     Cancel a command authentication attempt and terminate its process.

    Args:
        integration_id (str):
        attempt_id (str):
        location (IntegrationCommandCancelLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        integration_id=integration_id,
attempt_id=attempt_id,
location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    integration_id: str,
    attempt_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: IntegrationCommandCancelLocationType0 | None | Unset = UNSET,

) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Cancel command connection

     Cancel a command authentication attempt and terminate its process.

    Args:
        integration_id (str):
        attempt_id (str):
        location (IntegrationCommandCancelLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        integration_id=integration_id,
attempt_id=attempt_id,
client=client,
location=location,

    )).parsed
