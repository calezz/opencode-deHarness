from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_cursor_error_encoded import InvalidCursorErrorEncoded
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.session_message_list_order_type_0 import SessionMessageListOrderType0
from ...models.session_message_list_type_type_0 import SessionMessageListTypeType0
from ...models.session_messages_response import SessionMessagesResponse
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.unknown_error_encoded import UnknownErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    limit: None | str | Unset = UNSET,
    order: None | SessionMessageListOrderType0 | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    type_: None | SessionMessageListTypeType0 | Unset = UNSET,

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
    elif isinstance(order, SessionMessageListOrderType0):
        json_order = order.value
    else:
        json_order = order
    params["order"] = json_order

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, SessionMessageListTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/{session_id}/message".format(session_id=quote(str(session_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SessionMessagesResponse.from_dict(response.json())



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

    if response.status_code == 404:
        response_404 = SessionNotFoundErrorEncoded.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = UnknownErrorEncoded.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: None | str | Unset = UNSET,
    order: None | SessionMessageListOrderType0 | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    type_: None | SessionMessageListTypeType0 | Unset = UNSET,

) -> Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Get session messages

     Retrieve projected messages for a session, optionally filtered by type. Items keep the requested
    order across pages; use cursor.next or cursor.previous to move through the ordered timeline, passing
    the same type filter on each page.

    Args:
        session_id (str):
        limit (None | str | Unset): Maximum number of messages to return. When omitted, the
            endpoint returns its default page size.
        order (None | SessionMessageListOrderType0 | Unset): Message order for the first page. Use
            desc for newest first or asc for oldest first.
        cursor (None | str | Unset):
        type_ (None | SessionMessageListTypeType0 | Unset): Filter by message type before
            pagination. When omitted, all message types are returned. Pass the same type when
            following cursors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
limit=limit,
order=order,
cursor=cursor,
type_=type_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: None | str | Unset = UNSET,
    order: None | SessionMessageListOrderType0 | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    type_: None | SessionMessageListTypeType0 | Unset = UNSET,

) -> InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Get session messages

     Retrieve projected messages for a session, optionally filtered by type. Items keep the requested
    order across pages; use cursor.next or cursor.previous to move through the ordered timeline, passing
    the same type filter on each page.

    Args:
        session_id (str):
        limit (None | str | Unset): Maximum number of messages to return. When omitted, the
            endpoint returns its default page size.
        order (None | SessionMessageListOrderType0 | Unset): Message order for the first page. Use
            desc for newest first or asc for oldest first.
        cursor (None | str | Unset):
        type_ (None | SessionMessageListTypeType0 | Unset): Filter by message type before
            pagination. When omitted, all message types are returned. Pass the same type when
            following cursors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,
limit=limit,
order=order,
cursor=cursor,
type_=type_,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: None | str | Unset = UNSET,
    order: None | SessionMessageListOrderType0 | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    type_: None | SessionMessageListTypeType0 | Unset = UNSET,

) -> Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Get session messages

     Retrieve projected messages for a session, optionally filtered by type. Items keep the requested
    order across pages; use cursor.next or cursor.previous to move through the ordered timeline, passing
    the same type filter on each page.

    Args:
        session_id (str):
        limit (None | str | Unset): Maximum number of messages to return. When omitted, the
            endpoint returns its default page size.
        order (None | SessionMessageListOrderType0 | Unset): Message order for the first page. Use
            desc for newest first or asc for oldest first.
        cursor (None | str | Unset):
        type_ (None | SessionMessageListTypeType0 | Unset): Filter by message type before
            pagination. When omitted, all message types are returned. Pass the same type when
            following cursors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
limit=limit,
order=order,
cursor=cursor,
type_=type_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: None | str | Unset = UNSET,
    order: None | SessionMessageListOrderType0 | Unset = UNSET,
    cursor: None | str | Unset = UNSET,
    type_: None | SessionMessageListTypeType0 | Unset = UNSET,

) -> InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Get session messages

     Retrieve projected messages for a session, optionally filtered by type. Items keep the requested
    order across pages; use cursor.next or cursor.previous to move through the ordered timeline, passing
    the same type filter on each page.

    Args:
        session_id (str):
        limit (None | str | Unset): Maximum number of messages to return. When omitted, the
            endpoint returns its default page size.
        order (None | SessionMessageListOrderType0 | Unset): Message order for the first page. Use
            desc for newest first or asc for oldest first.
        cursor (None | str | Unset):
        type_ (None | SessionMessageListTypeType0 | Unset): Filter by message type before
            pagination. When omitted, all message types are returned. Pass the same type when
            following cursors.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidCursorErrorEncoded | InvalidRequestErrorEncoded | SessionMessagesResponse | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
limit=limit,
order=order,
cursor=cursor,
type_=type_,

    )).parsed
