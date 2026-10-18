from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/location/reload",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 503:
        response_503 = ServiceUnavailableErrorEncoded.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ Reload configuration

     Shut down and rebuild every loaded location. Pending permissions and forms are cancelled; running
    sessions continue with fresh services at the next step boundary. Emits location.shutdown for client
    recovery and responds once all replacement builds settle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Reload configuration

     Shut down and rebuild every loaded location. Pending permissions and forms are cancelled; running
    sessions continue with fresh services at the next step boundary. Emits location.shutdown for client
    recovery and responds once all replacement builds settle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]:
    """ Reload configuration

     Shut down and rebuild every loaded location. Pending permissions and forms are cancelled; running
    sessions continue with fresh services at the next step boundary. Emits location.shutdown for client
    recovery and responds once all replacement builds settle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Reload configuration

     Shut down and rebuild every loaded location. Pending permissions and forms are cancelled; running
    sessions continue with fresh services at the next step boundary. Emits location.shutdown for client
    recovery and responds once all replacement builds settle.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
