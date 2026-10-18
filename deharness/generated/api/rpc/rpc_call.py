from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.rpc_call_location_type_0 import RpcCallLocationType0
from ...models.rpc_error_encoded import RpcErrorEncoded
from ...models.rpc_input import RpcInput
from ...models.rpc_internal_error_encoded import RpcInternalErrorEncoded
from ...models.rpc_output import RpcOutput
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    rpc_id: str,
    method: str,
    *,
    body: RpcInput,
    location: None | RpcCallLocationType0 | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, RpcCallLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/rpc/{rpc_id}/{method}".format(rpc_id=quote(str(rpc_id), safe=""),method=quote(str(method), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = RpcOutput.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        def _parse_response_400(data: object) -> InvalidRequestErrorEncoded | RpcErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = RpcErrorEncoded.from_dict(data)



                return response_400_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_400_type_1 = InvalidRequestErrorEncoded.from_dict(data)



            return response_400_type_1

        response_400 = _parse_response_400(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = LocationNotFoundErrorEncoded.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = RpcInternalErrorEncoded.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    rpc_id: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,
    body: RpcInput,
    location: None | RpcCallLocationType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded]:
    """ Call a plugin RPC

     Dispatch a method to the currently registered RPC at the requested location.

    Args:
        rpc_id (str):
        method (str):
        location (None | RpcCallLocationType0 | Unset):
        body (RpcInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        rpc_id=rpc_id,
method=method,
body=body,
location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    rpc_id: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,
    body: RpcInput,
    location: None | RpcCallLocationType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded | None:
    """ Call a plugin RPC

     Dispatch a method to the currently registered RPC at the requested location.

    Args:
        rpc_id (str):
        method (str):
        location (None | RpcCallLocationType0 | Unset):
        body (RpcInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        rpc_id=rpc_id,
method=method,
client=client,
body=body,
location=location,

    ).parsed

async def asyncio_detailed(
    rpc_id: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,
    body: RpcInput,
    location: None | RpcCallLocationType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded]:
    """ Call a plugin RPC

     Dispatch a method to the currently registered RPC at the requested location.

    Args:
        rpc_id (str):
        method (str):
        location (None | RpcCallLocationType0 | Unset):
        body (RpcInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        rpc_id=rpc_id,
method=method,
body=body,
location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    rpc_id: str,
    method: str,
    *,
    client: AuthenticatedClient | Client,
    body: RpcInput,
    location: None | RpcCallLocationType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded | None:
    """ Call a plugin RPC

     Dispatch a method to the currently registered RPC at the requested location.

    Args:
        rpc_id (str):
        method (str):
        location (None | RpcCallLocationType0 | Unset):
        body (RpcInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | RpcErrorEncoded | LocationNotFoundErrorEncoded | RpcInternalErrorEncoded | RpcOutput | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        rpc_id=rpc_id,
method=method,
client=client,
body=body,
location=location,

    )).parsed
