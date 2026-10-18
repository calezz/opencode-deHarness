from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.message_not_found_error_encoded import MessageNotFoundErrorEncoded
from ...models.session_diff_response_200 import SessionDiffResponse200
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.unknown_error_encoded import UnknownErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    context: None | str | Unset = UNSET,

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

    json_context: None | str | Unset
    if isinstance(context, Unset):
        json_context = UNSET
    else:
        json_context = context
    params["context"] = json_context


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/session/{session_id}/diff".format(session_id=quote(str(session_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SessionDiffResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        def _parse_response_404(data: object) -> LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = MessageNotFoundErrorEncoded.from_dict(data)



                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_1 = SessionNotFoundErrorEncoded.from_dict(data)



                return response_404_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_2 = LocationNotFoundErrorEncoded.from_dict(data)



            return response_404_type_2

        response_404 = _parse_response_404(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = UnknownErrorEncoded.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
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
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Diff session turns

     Structured per-file diffs of the files a turn changed. A turn runs from the first prompt after the
    session was last idle until its next idle marker, so prompts steered in while it was busy belong to
    the same turn; `to` extends the range through a later turn. Compares the range's first recorded
    snapshot with its last; a step still running in the active session compares against the working
    copy. Ranges that span a location change are rejected. In sessions without any idle marker, a
    prompt's turn spans until the next user message.

    Args:
        session_id (str):
        from_ (None | str | Unset): User message whose turn to diff. Defaults to the turn of the
            newest user message.
        to (None | str | Unset): Later user message whose turn ends the range. Defaults to the
            turn of `from` alone.
        context (None | str | Unset): Unchanged lines around each hunk. Omit for full-file
            patches.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
from_=from_,
to=to,
context=context,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Diff session turns

     Structured per-file diffs of the files a turn changed. A turn runs from the first prompt after the
    session was last idle until its next idle marker, so prompts steered in while it was busy belong to
    the same turn; `to` extends the range through a later turn. Compares the range's first recorded
    snapshot with its last; a step still running in the active session compares against the working
    copy. Ranges that span a location change are rejected. In sessions without any idle marker, a
    prompt's turn spans until the next user message.

    Args:
        session_id (str):
        from_ (None | str | Unset): User message whose turn to diff. Defaults to the turn of the
            newest user message.
        to (None | str | Unset): Later user message whose turn ends the range. Defaults to the
            turn of `from` alone.
        context (None | str | Unset): Unchanged lines around each hunk. Omit for full-file
            patches.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,
from_=from_,
to=to,
context=context,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Diff session turns

     Structured per-file diffs of the files a turn changed. A turn runs from the first prompt after the
    session was last idle until its next idle marker, so prompts steered in while it was busy belong to
    the same turn; `to` extends the range through a later turn. Compares the range's first recorded
    snapshot with its last; a step still running in the active session compares against the working
    copy. Ranges that span a location change are rejected. In sessions without any idle marker, a
    prompt's turn spans until the next user message.

    Args:
        session_id (str):
        from_ (None | str | Unset): User message whose turn to diff. Defaults to the turn of the
            newest user message.
        to (None | str | Unset): Later user message whose turn ends the range. Defaults to the
            turn of `from` alone.
        context (None | str | Unset): Unchanged lines around each hunk. Omit for full-file
            patches.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
from_=from_,
to=to,
context=context,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    from_: None | str | Unset = UNSET,
    to: None | str | Unset = UNSET,
    context: None | str | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Diff session turns

     Structured per-file diffs of the files a turn changed. A turn runs from the first prompt after the
    session was last idle until its next idle marker, so prompts steered in while it was busy belong to
    the same turn; `to` extends the range through a later turn. Compares the range's first recorded
    snapshot with its last; a step still running in the active session compares against the working
    copy. Ranges that span a location change are rejected. In sessions without any idle marker, a
    prompt's turn spans until the next user message.

    Args:
        session_id (str):
        from_ (None | str | Unset): User message whose turn to diff. Defaults to the turn of the
            newest user message.
        to (None | str | Unset): Later user message whose turn ends the range. Defaults to the
            turn of `from` alone.
        context (None | str | Unset): Unchanged lines around each hunk. Omit for full-file
            patches.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionDiffResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
from_=from_,
to=to,
context=context,

    )).parsed
