from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.agent_get_location_type_0 import AgentGetLocationType0
from ...models.agent_get_response_200 import AgentGetResponse200
from ...models.agent_not_found_error_encoded import AgentNotFoundErrorEncoded
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    agent_id: str,
    *,
    location: AgentGetLocationType0 | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_location: dict[str, Any] | None | Unset
    if isinstance(location, Unset):
        json_location = UNSET
    elif isinstance(location, AgentGetLocationType0):
        json_location = location.to_dict()
    else:
        json_location = location
    params["location"] = json_location


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/agent/{agent_id}".format(agent_id=quote(str(agent_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = AgentGetResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        def _parse_response_404(data: object) -> AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = AgentNotFoundErrorEncoded.from_dict(data)



                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = LocationNotFoundErrorEncoded.from_dict(data)



            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: AgentGetLocationType0 | None | Unset = UNSET,

) -> Response[AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Get agent

     Retrieve a single currently registered agent.

    Args:
        agent_id (str):
        location (AgentGetLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
location=location,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: AgentGetLocationType0 | None | Unset = UNSET,

) -> AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Get agent

     Retrieve a single currently registered agent.

    Args:
        agent_id (str):
        location (AgentGetLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        agent_id=agent_id,
client=client,
location=location,

    ).parsed

async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: AgentGetLocationType0 | None | Unset = UNSET,

) -> Response[AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Get agent

     Retrieve a single currently registered agent.

    Args:
        agent_id (str):
        location (AgentGetLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        agent_id=agent_id,
location=location,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient | Client,
    location: AgentGetLocationType0 | None | Unset = UNSET,

) -> AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Get agent

     Retrieve a single currently registered agent.

    Args:
        agent_id (str):
        location (AgentGetLocationType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentGetResponse200 | AgentNotFoundErrorEncoded | LocationNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        agent_id=agent_id,
client=client,
location=location,

    )).parsed
