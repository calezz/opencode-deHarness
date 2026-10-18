from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.session_log_follow_type_0 import SessionLogFollowType0
from ...models.session_log_response_200 import SessionLogResponse200
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    after: None | str | Unset = UNSET,
    follow: None | SessionLogFollowType0 | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_after: None | str | Unset
    if isinstance(after, Unset):
        json_after = UNSET
    else:
        json_after = after
    params["after"] = json_after

    json_follow: None | str | Unset
    if isinstance(follow, Unset):
        json_follow = UNSET
    elif isinstance(follow, SessionLogFollowType0):
        json_follow = follow.value
    else:
        json_follow = follow
    params["follow"] = json_follow


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/experimental/session/{session_id}/log".format(session_id=quote(str(session_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SessionLogResponse200.from_dict(response.text)



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = SessionNotFoundErrorEncoded.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
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
    after: None | str | Unset = UNSET,
    follow: None | SessionLogFollowType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Read the session log

     Experimental durable session event log. Reads events after an exclusive aggregate sequence and
    continues with live events when follow=true.

    Args:
        session_id (str):
        after (None | str | Unset):
        follow (None | SessionLogFollowType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
after=after,
follow=follow,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: None | str | Unset = UNSET,
    follow: None | SessionLogFollowType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Read the session log

     Experimental durable session event log. Reads events after an exclusive aggregate sequence and
    continues with live events when follow=true.

    Args:
        session_id (str):
        after (None | str | Unset):
        follow (None | SessionLogFollowType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,
after=after,
follow=follow,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: None | str | Unset = UNSET,
    follow: None | SessionLogFollowType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Read the session log

     Experimental durable session event log. Reads events after an exclusive aggregate sequence and
    continues with live events when follow=true.

    Args:
        session_id (str):
        after (None | str | Unset):
        follow (None | SessionLogFollowType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
after=after,
follow=follow,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    after: None | str | Unset = UNSET,
    follow: None | SessionLogFollowType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Read the session log

     Experimental durable session event log. Reads events after an exclusive aggregate sequence and
    continues with live events when follow=true.

    Args:
        session_id (str):
        after (None | str | Unset):
        follow (None | SessionLogFollowType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | SessionLogResponse200 | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
after=after,
follow=follow,

    )).parsed
