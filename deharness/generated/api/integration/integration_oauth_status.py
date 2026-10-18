from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integration_attempt_not_found_error_encoded import IntegrationAttemptNotFoundErrorEncoded
from ...models.integration_not_found_error_encoded import IntegrationNotFoundErrorEncoded
from ...models.integration_oauth_status_location_type_0 import IntegrationOauthStatusLocationType0
from ...models.integration_oauth_status_response_200 import IntegrationOauthStatusResponse200
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    integration_id: str,
    attempt_id: str,
    *,
    location: IntegrationOauthStatusLocationType0 | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, IntegrationOauthStatusLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/integration/{integration_id}/connect/oauth/{attempt_id}".format(integration_id=quote(str(integration_id), safe=""),attempt_id=quote(str(attempt_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = IntegrationOauthStatusResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        def _parse_response_404(data: object) -> IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = IntegrationNotFoundErrorEncoded.from_dict(data)



                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_1 = IntegrationAttemptNotFoundErrorEncoded.from_dict(data)



                return response_404_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_2 = LocationNotFoundErrorEncoded.from_dict(data)



            return response_404_type_2

        response_404 = _parse_response_404(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
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
    location: IntegrationOauthStatusLocationType0 | None | Unset = UNSET,

) -> Response[IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Get OAuth attempt status

     Poll the current status of an OAuth attempt.

    Args:
        integration_id (str):
        attempt_id (str):
        location (IntegrationOauthStatusLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
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
    location: IntegrationOauthStatusLocationType0 | None | Unset = UNSET,

) -> IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Get OAuth attempt status

     Poll the current status of an OAuth attempt.

    Args:
        integration_id (str):
        attempt_id (str):
        location (IntegrationOauthStatusLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
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
    location: IntegrationOauthStatusLocationType0 | None | Unset = UNSET,

) -> Response[IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Get OAuth attempt status

     Poll the current status of an OAuth attempt.

    Args:
        integration_id (str):
        attempt_id (str):
        location (IntegrationOauthStatusLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
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
    location: IntegrationOauthStatusLocationType0 | None | Unset = UNSET,

) -> IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Get OAuth attempt status

     Poll the current status of an OAuth attempt.

    Args:
        integration_id (str):
        attempt_id (str):
        location (IntegrationOauthStatusLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationAttemptNotFoundErrorEncoded | IntegrationNotFoundErrorEncoded | LocationNotFoundErrorEncoded | IntegrationOauthStatusResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        integration_id=integration_id,
attempt_id=attempt_id,
client=client,
location=location,

    )).parsed
