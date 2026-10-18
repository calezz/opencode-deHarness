from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.experimental_fs_write_location_type_0 import ExperimentalFsWriteLocationType0
from ...models.experimental_fs_write_response_200 import ExperimentalFsWriteResponse200
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import File, FileTypes
from ...types import UNSET, Unset
from io import BytesIO
from typing import cast



def _get_kwargs(
    *,
    body: File,
    location: ExperimentalFsWriteLocationType0 | None | Unset = UNSET,
    path: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, ExperimentalFsWriteLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location

    params["path"] = path


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/experimental/fs/write",
        "params": params,
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = ExperimentalFsWriteResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    location: ExperimentalFsWriteLocationType0 | None | Unset = UNSET,
    path: str,

) -> Response[ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Write file

     Write the raw request body to an absolute path or a path relative to the requested location,
    creating parent directories, and return the resolved absolute path. Unlike read, the target is not
    confined to the location. Experimental: may change without compatibility guarantees.

    Args:
        location (ExperimentalFsWriteLocationType0 | None | Unset):
        path (str): An absolute path or a path relative to the requested location. Missing parent
            directories are created.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        body=body,
location=location,
path=path,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    location: ExperimentalFsWriteLocationType0 | None | Unset = UNSET,
    path: str,

) -> ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Write file

     Write the raw request body to an absolute path or a path relative to the requested location,
    creating parent directories, and return the resolved absolute path. Unlike read, the target is not
    confined to the location. Experimental: may change without compatibility guarantees.

    Args:
        location (ExperimentalFsWriteLocationType0 | None | Unset):
        path (str): An absolute path or a path relative to the requested location. Missing parent
            directories are created.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,
body=body,
location=location,
path=path,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    location: ExperimentalFsWriteLocationType0 | None | Unset = UNSET,
    path: str,

) -> Response[ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Write file

     Write the raw request body to an absolute path or a path relative to the requested location,
    creating parent directories, and return the resolved absolute path. Unlike read, the target is not
    confined to the location. Experimental: may change without compatibility guarantees.

    Args:
        location (ExperimentalFsWriteLocationType0 | None | Unset):
        path (str): An absolute path or a path relative to the requested location. Missing parent
            directories are created.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        body=body,
location=location,
path=path,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: File,
    location: ExperimentalFsWriteLocationType0 | None | Unset = UNSET,
    path: str,

) -> ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Write file

     Write the raw request body to an absolute path or a path relative to the requested location,
    creating parent directories, and return the resolved absolute path. Unlike read, the target is not
    confined to the location. Experimental: may change without compatibility guarantees.

    Args:
        location (ExperimentalFsWriteLocationType0 | None | Unset):
        path (str): An absolute path or a path relative to the requested location. Missing parent
            directories are created.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentalFsWriteResponse200 | InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
body=body,
location=location,
path=path,

    )).parsed
