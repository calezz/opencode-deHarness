from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.experimental_voice_session_body import ExperimentalVoiceSessionBody
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.voice_session_response import VoiceSessionResponse
from typing import cast



def _get_kwargs(
    *,
    body: ExperimentalVoiceSessionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/experimental/voice/session",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse | None:
    if response.status_code == 200:
        response_200 = VoiceSessionResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalVoiceSessionBody,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse]:
    """ Create voice session

     Create a server-brokered voice session using the server's configured provider credentials and return
    the WebRTC SDP answer or WebSocket ephemeral token.

    Args:
        body (ExperimentalVoiceSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalVoiceSessionBody,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse | None:
    """ Create voice session

     Create a server-brokered voice session using the server's configured provider credentials and return
    the WebRTC SDP answer or WebSocket ephemeral token.

    Args:
        body (ExperimentalVoiceSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalVoiceSessionBody,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse]:
    """ Create voice session

     Create a server-brokered voice session using the server's configured provider credentials and return
    the WebRTC SDP answer or WebSocket ephemeral token.

    Args:
        body (ExperimentalVoiceSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalVoiceSessionBody,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse | None:
    """ Create voice session

     Create a server-brokered voice session using the server's configured provider credentials and return
    the WebRTC SDP answer or WebSocket ephemeral token.

    Args:
        body (ExperimentalVoiceSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VoiceSessionResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
