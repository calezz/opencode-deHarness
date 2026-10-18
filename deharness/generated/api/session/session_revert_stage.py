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
from ...models.session_busy_error_encoded import SessionBusyErrorEncoded
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.session_revert_stage_body import SessionRevertStageBody
from ...models.session_revert_stage_response_200 import SessionRevertStageResponse200
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.unknown_error_encoded import UnknownErrorEncoded
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    body: SessionRevertStageBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/session/{session_id}/revert/stage".format(session_id=quote(str(session_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SessionRevertStageResponse200.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = SessionBusyErrorEncoded.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = UnknownErrorEncoded.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
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
    body: SessionRevertStageBody,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Stage session revert

     Stage or move a reversible session boundary and optionally apply its file changes.

    Args:
        session_id (str):
        body (SessionRevertStageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SessionRevertStageBody,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Stage session revert

     Stage or move a reversible session boundary and optionally apply its file changes.

    Args:
        session_id (str):
        body (SessionRevertStageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SessionRevertStageBody,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Stage session revert

     Stage or move a reversible session boundary and optionally apply its file changes.

    Args:
        session_id (str):
        body (SessionRevertStageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SessionRevertStageBody,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Stage session revert

     Stage or move a reversible session boundary and optionally apply its file changes.

    Args:
        session_id (str):
        body (SessionRevertStageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | MessageNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionBusyErrorEncoded | SessionRevertStageResponse200 | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
body=body,

    )).parsed
