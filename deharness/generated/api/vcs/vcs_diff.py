from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.service_unavailable_error_encoded import ServiceUnavailableErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.vcs_diff_location_type_0 import VcsDiffLocationType0
from ...models.vcs_diff_response_200 import VcsDiffResponse200
from ...models.vcs_mode import VcsMode
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    location: None | Unset | VcsDiffLocationType0 = UNSET,
    mode: VcsMode,
    base: str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, VcsDiffLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location

    json_mode = mode.value
    params["mode"] = json_mode

    params["base"] = base

    json_context: None | str | Unset
    if isinstance(context, Unset):
        json_context = UNSET
    else:
        json_context = context
    params["context"] = json_context


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/vcs/diff",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200 | None:
    if response.status_code == 200:
        response_200 = VcsDiffResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsDiffLocationType0 = UNSET,
    mode: VcsMode,
    base: str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200]:
    """ VCS diff

     Diff HEAD to the working copy (working), the base merge-base to the working copy (branch), or the
    base merge-base to HEAD (committed). Omitting base preserves repository-default comparison;
    supplying it overrides the comparison without saving it.

    Args:
        location (None | Unset | VcsDiffLocationType0):
        mode (VcsMode):
        base (str | Unset):
        context (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200]
     """


    kwargs = _get_kwargs(
        location=location,
mode=mode,
base=base,
context=context,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsDiffLocationType0 = UNSET,
    mode: VcsMode,
    base: str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200 | None:
    """ VCS diff

     Diff HEAD to the working copy (working), the base merge-base to the working copy (branch), or the
    base merge-base to HEAD (committed). Omitting base preserves repository-default comparison;
    supplying it overrides the comparison without saving it.

    Args:
        location (None | Unset | VcsDiffLocationType0):
        mode (VcsMode):
        base (str | Unset):
        context (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200
     """


    return sync_detailed(
        client=client,
location=location,
mode=mode,
base=base,
context=context,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsDiffLocationType0 = UNSET,
    mode: VcsMode,
    base: str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200]:
    """ VCS diff

     Diff HEAD to the working copy (working), the base merge-base to the working copy (branch), or the
    base merge-base to HEAD (committed). Omitting base preserves repository-default comparison;
    supplying it overrides the comparison without saving it.

    Args:
        location (None | Unset | VcsDiffLocationType0):
        mode (VcsMode):
        base (str | Unset):
        context (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200]
     """


    kwargs = _get_kwargs(
        location=location,
mode=mode,
base=base,
context=context,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    location: None | Unset | VcsDiffLocationType0 = UNSET,
    mode: VcsMode,
    base: str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200 | None:
    """ VCS diff

     Diff HEAD to the working copy (working), the base merge-base to the working copy (branch), or the
    base merge-base to HEAD (committed). Omitting base preserves repository-default comparison;
    supplying it overrides the comparison without saving it.

    Args:
        location (None | Unset | VcsDiffLocationType0):
        mode (VcsMode):
        base (str | Unset):
        context (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ServiceUnavailableErrorEncoded | UnauthorizedErrorEncoded | VcsDiffResponse200
     """


    return (await asyncio_detailed(
        client=client,
location=location,
mode=mode,
base=base,
context=context,

    )).parsed
