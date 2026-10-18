from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integration_oauth_connect_body import IntegrationOauthConnectBody
from ...models.integration_oauth_connect_location_type_0 import IntegrationOauthConnectLocationType0
from ...models.integration_oauth_connect_response_200 import IntegrationOauthConnectResponse200
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    integration_id: str,
    *,
    body: IntegrationOauthConnectBody,
    location: IntegrationOauthConnectLocationType0 | None | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, IntegrationOauthConnectLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/integration/{integration_id}/connect/oauth".format(integration_id=quote(str(integration_id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = IntegrationOauthConnectResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IntegrationOauthConnectBody,
    location: IntegrationOauthConnectLocationType0 | None | Unset = UNSET,

) -> Response[IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Begin OAuth connection

     Start an OAuth attempt and return the authorization details.

    Args:
        integration_id (str):
        location (IntegrationOauthConnectLocationType0 | None | Unset):
        body (IntegrationOauthConnectBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        integration_id=integration_id,
body=body,
location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    integration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IntegrationOauthConnectBody,
    location: IntegrationOauthConnectLocationType0 | None | Unset = UNSET,

) -> IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Begin OAuth connection

     Start an OAuth attempt and return the authorization details.

    Args:
        integration_id (str):
        location (IntegrationOauthConnectLocationType0 | None | Unset):
        body (IntegrationOauthConnectBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        integration_id=integration_id,
client=client,
body=body,
location=location,

    ).parsed

async def asyncio_detailed(
    integration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IntegrationOauthConnectBody,
    location: IntegrationOauthConnectLocationType0 | None | Unset = UNSET,

) -> Response[IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Begin OAuth connection

     Start an OAuth attempt and return the authorization details.

    Args:
        integration_id (str):
        location (IntegrationOauthConnectLocationType0 | None | Unset):
        body (IntegrationOauthConnectBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        integration_id=integration_id,
body=body,
location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    integration_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IntegrationOauthConnectBody,
    location: IntegrationOauthConnectLocationType0 | None | Unset = UNSET,

) -> IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Begin OAuth connection

     Start an OAuth attempt and return the authorization details.

    Args:
        integration_id (str):
        location (IntegrationOauthConnectLocationType0 | None | Unset):
        body (IntegrationOauthConnectBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationOauthConnectResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        integration_id=integration_id,
client=client,
body=body,
location=location,

    )).parsed
