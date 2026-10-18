from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.experimental_session_stats_response_200 import ExperimentalSessionStatsResponse200
from ...models.experimental_session_stats_tools_type_0 import ExperimentalSessionStatsToolsType0
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    tools: ExperimentalSessionStatsToolsType0 | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_: None | str | Unset
    if isinstance(from_, Unset):
        json_from_ = UNSET
    else:
        json_from_ = from_
    params["from"] = json_from_

    json_to: None | str | Unset
    if isinstance(to, Unset):
        json_to = UNSET
    else:
        json_to = to
    params["to"] = json_to

    json_project: None | str | Unset
    if isinstance(project, Unset):
        json_project = UNSET
    else:
        json_project = project
    params["project"] = json_project

    json_timezone: None | str | Unset
    if isinstance(timezone, Unset):
        json_timezone = UNSET
    else:
        json_timezone = timezone
    params["timezone"] = json_timezone

    json_tools: None | str | Unset
    if isinstance(tools, Unset):
        json_tools = UNSET
    elif isinstance(tools, ExperimentalSessionStatsToolsType0):
        json_tools = tools.value
    else:
        json_tools = tools
    params["tools"] = json_tools


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/experimental/session/stats",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = ExperimentalSessionStatsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    tools: ExperimentalSessionStatsToolsType0 | None | Unset = UNSET,

) -> Response[ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Get session statistics

     Aggregate local session activity, usage, and tool reliability for a time range.

    Args:
        from_ (None | str | Unset):
        to (None | str | Unset):
        project (None | str | Unset):
        timezone (None | str | Unset):
        tools (ExperimentalSessionStatsToolsType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,
project=project,
timezone=timezone,
tools=tools,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    tools: ExperimentalSessionStatsToolsType0 | None | Unset = UNSET,

) -> ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Get session statistics

     Aggregate local session activity, usage, and tool reliability for a time range.

    Args:
        from_ (None | str | Unset):
        to (None | str | Unset):
        project (None | str | Unset):
        timezone (None | str | Unset):
        tools (ExperimentalSessionStatsToolsType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,
from_=from_,
to=to,
project=project,
timezone=timezone,
tools=tools,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    tools: ExperimentalSessionStatsToolsType0 | None | Unset = UNSET,

) -> Response[ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Get session statistics

     Aggregate local session activity, usage, and tool reliability for a time range.

    Args:
        from_ (None | str | Unset):
        to (None | str | Unset):
        project (None | str | Unset):
        timezone (None | str | Unset):
        tools (ExperimentalSessionStatsToolsType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        from_=from_,
to=to,
project=project,
timezone=timezone,
tools=tools,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    timezone: None | str | Unset = UNSET,
    tools: ExperimentalSessionStatsToolsType0 | None | Unset = UNSET,

) -> ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Get session statistics

     Aggregate local session activity, usage, and tool reliability for a time range.

    Args:
        from_ (None | str | Unset):
        to (None | str | Unset):
        project (None | str | Unset):
        timezone (None | str | Unset):
        tools (ExperimentalSessionStatsToolsType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentalSessionStatsResponse200 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
from_=from_,
to=to,
project=project,
timezone=timezone,
tools=tools,

    )).parsed
