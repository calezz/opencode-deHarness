from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_cursor_error_encoded import InvalidCursorErrorEncoded
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.session_list_order_type_0 import SessionListOrderType0
from ...models.session_list_parent_id_type_0_type_1 import SessionListParentIDType0Type1
from ...models.sessions_response import SessionsResponse
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    limit: None | str | Unset = UNSET,
    order: None | SessionListOrderType0 | Unset = UNSET,
    search: None | str | Unset = UNSET,
    parent_id: None | SessionListParentIDType0Type1 | str | Unset = UNSET,
    directory: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    subpath: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_limit: None | str | Unset
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_order: None | str | Unset
    if isinstance(order, Unset):
        json_order = UNSET
    elif isinstance(order, SessionListOrderType0):
        json_order = order.value
    else:
        json_order = order
    params["order"] = json_order

    json_search: None | str | Unset
    if isinstance(search, Unset):
        json_search = UNSET
    else:
        json_search = search
    params["search"] = json_search

    json_parent_id: None | str | Unset
    if isinstance(parent_id, Unset):
        json_parent_id = UNSET
    elif isinstance(parent_id, SessionListParentIDType0Type1):
        json_parent_id = parent_id.value
    else:
        json_parent_id = parent_id
    params["parentID"] = json_parent_id

    json_directory: None | str | Unset
    if isinstance(directory, Unset):
        json_directory = UNSET
    else:
        json_directory = directory
    params["directory"] = json_directory

    json_project: None | str | Unset
    if isinstance(project, Unset):
        json_project = UNSET
    else:
        json_project = project
    params["project"] = json_project

    json_subpath: None | str | Unset
    if isinstance(subpath, Unset):
        json_subpath = UNSET
    else:
        json_subpath = subpath
    params["subpath"] = json_subpath

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SessionsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        def _parse_response_400(data: object) -> InvalidCursorErrorEncoded | InvalidRequestErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = InvalidCursorErrorEncoded.from_dict(data)



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: None | str | Unset = UNSET,
    order: None | SessionListOrderType0 | Unset = UNSET,
    search: None | str | Unset = UNSET,
    parent_id: None | SessionListParentIDType0Type1 | str | Unset = UNSET,
    directory: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    subpath: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,

) -> Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded]:
    """ List sessions

     Retrieve sessions in the requested order. Items keep that order across pages; use cursor.next or
    cursor.previous to move through the ordered list.

    Args:
        limit (None | str | Unset): Maximum number of sessions to return. Defaults to the newest
            50 sessions.
        order (None | SessionListOrderType0 | Unset): Session order for the first page. Use desc
            for newest first or asc for oldest first.
        search (None | str | Unset):
        parent_id (None | SessionListParentIDType0Type1 | str | Unset):
        directory (None | str | Unset):
        project (None | str | Unset):
        subpath (None | str | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        limit=limit,
order=order,
search=search,
parent_id=parent_id,
directory=directory,
project=project,
subpath=subpath,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: None | str | Unset = UNSET,
    order: None | SessionListOrderType0 | Unset = UNSET,
    search: None | str | Unset = UNSET,
    parent_id: None | SessionListParentIDType0Type1 | str | Unset = UNSET,
    directory: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    subpath: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,

) -> InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded | None:
    """ List sessions

     Retrieve sessions in the requested order. Items keep that order across pages; use cursor.next or
    cursor.previous to move through the ordered list.

    Args:
        limit (None | str | Unset): Maximum number of sessions to return. Defaults to the newest
            50 sessions.
        order (None | SessionListOrderType0 | Unset): Session order for the first page. Use desc
            for newest first or asc for oldest first.
        search (None | str | Unset):
        parent_id (None | SessionListParentIDType0Type1 | str | Unset):
        directory (None | str | Unset):
        project (None | str | Unset):
        subpath (None | str | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,
limit=limit,
order=order,
search=search,
parent_id=parent_id,
directory=directory,
project=project,
subpath=subpath,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: None | str | Unset = UNSET,
    order: None | SessionListOrderType0 | Unset = UNSET,
    search: None | str | Unset = UNSET,
    parent_id: None | SessionListParentIDType0Type1 | str | Unset = UNSET,
    directory: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    subpath: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,

) -> Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded]:
    """ List sessions

     Retrieve sessions in the requested order. Items keep that order across pages; use cursor.next or
    cursor.previous to move through the ordered list.

    Args:
        limit (None | str | Unset): Maximum number of sessions to return. Defaults to the newest
            50 sessions.
        order (None | SessionListOrderType0 | Unset): Session order for the first page. Use desc
            for newest first or asc for oldest first.
        search (None | str | Unset):
        parent_id (None | SessionListParentIDType0Type1 | str | Unset):
        directory (None | str | Unset):
        project (None | str | Unset):
        subpath (None | str | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        limit=limit,
order=order,
search=search,
parent_id=parent_id,
directory=directory,
project=project,
subpath=subpath,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: None | str | Unset = UNSET,
    order: None | SessionListOrderType0 | Unset = UNSET,
    search: None | str | Unset = UNSET,
    parent_id: None | SessionListParentIDType0Type1 | str | Unset = UNSET,
    directory: None | str | Unset = UNSET,
    project: None | str | Unset = UNSET,
    subpath: None | str | Unset = UNSET,
    cursor: None | str | Unset = UNSET,

) -> InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded | None:
    """ List sessions

     Retrieve sessions in the requested order. Items keep that order across pages; use cursor.next or
    cursor.previous to move through the ordered list.

    Args:
        limit (None | str | Unset): Maximum number of sessions to return. Defaults to the newest
            50 sessions.
        order (None | SessionListOrderType0 | Unset): Session order for the first page. Use desc
            for newest first or asc for oldest first.
        search (None | str | Unset):
        parent_id (None | SessionListParentIDType0Type1 | str | Unset):
        directory (None | str | Unset):
        project (None | str | Unset):
        subpath (None | str | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionsResponse | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
order=order,
search=search,
parent_id=parent_id,
directory=directory,
project=project,
subpath=subpath,
cursor=cursor,

    )).parsed
