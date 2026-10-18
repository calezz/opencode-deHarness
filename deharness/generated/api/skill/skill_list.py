from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.skill_list_location_type_0 import SkillListLocationType0
from ...models.skill_list_response_200 import SkillListResponse200
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    location: None | SkillListLocationType0 | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, SkillListLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/skill",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SkillListResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: None | SkillListLocationType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded]:
    """ List skills

     Retrieve currently registered skills.

    Args:
        location (None | SkillListLocationType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    location: None | SkillListLocationType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded | None:
    """ List skills

     Retrieve currently registered skills.

    Args:
        location (None | SkillListLocationType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,
location=location,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    location: None | SkillListLocationType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded]:
    """ List skills

     Retrieve currently registered skills.

    Args:
        location (None | SkillListLocationType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    location: None | SkillListLocationType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded | None:
    """ List skills

     Retrieve currently registered skills.

    Args:
        location (None | SkillListLocationType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SkillListResponse200 | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
location=location,

    )).parsed
