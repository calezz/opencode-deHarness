from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.experimental_mcp_add_body import ExperimentalMcpAddBody
from ...models.experimental_mcp_add_location_type_0 import ExperimentalMcpAddLocationType0
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    server: str,
    *,
    body: ExperimentalMcpAddBody,
    location: ExperimentalMcpAddLocationType0 | None | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, ExperimentalMcpAddLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/experimental/mcp/{server}".format(server=quote(str(server), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    server: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalMcpAddBody,
    location: ExperimentalMcpAddLocationType0 | None | Unset = UNSET,

) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Add MCP server

     Add an MCP server at runtime or replace an existing one, connecting it immediately.

    Args:
        server (str):
        location (ExperimentalMcpAddLocationType0 | None | Unset):
        body (ExperimentalMcpAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        server=server,
body=body,
location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    server: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalMcpAddBody,
    location: ExperimentalMcpAddLocationType0 | None | Unset = UNSET,

) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Add MCP server

     Add an MCP server at runtime or replace an existing one, connecting it immediately.

    Args:
        server (str):
        location (ExperimentalMcpAddLocationType0 | None | Unset):
        body (ExperimentalMcpAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        server=server,
client=client,
body=body,
location=location,

    ).parsed

async def asyncio_detailed(
    server: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalMcpAddBody,
    location: ExperimentalMcpAddLocationType0 | None | Unset = UNSET,

) -> Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Add MCP server

     Add an MCP server at runtime or replace an existing one, connecting it immediately.

    Args:
        server (str):
        location (ExperimentalMcpAddLocationType0 | None | Unset):
        body (ExperimentalMcpAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        server=server,
body=body,
location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    server: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalMcpAddBody,
    location: ExperimentalMcpAddLocationType0 | None | Unset = UNSET,

) -> Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Add MCP server

     Add an MCP server at runtime or replace an existing one, connecting it immediately.

    Args:
        server (str):
        location (ExperimentalMcpAddLocationType0 | None | Unset):
        body (ExperimentalMcpAddBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        server=server,
client=client,
body=body,
location=location,

    )).parsed
