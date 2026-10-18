from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.experimental_session_export_response_200 import ExperimentalSessionExportResponse200
from ...models.experimental_session_export_sanitize_type_0 import ExperimentalSessionExportSanitizeType0
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.unknown_error_encoded import UnknownErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    sanitize: ExperimentalSessionExportSanitizeType0 | None | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_sanitize: None | str | Unset
    if isinstance(sanitize, Unset):
        json_sanitize = UNSET
    elif isinstance(sanitize, ExperimentalSessionExportSanitizeType0):
        json_sanitize = sanitize.value
    else:
        json_sanitize = sanitize
    params["sanitize"] = json_sanitize


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/experimental/session/{session_id}/export".format(session_id=quote(str(session_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    if response.status_code == 200:
        response_200 = ExperimentalSessionExportResponse200.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = UnknownErrorEncoded.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
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
    sanitize: ExperimentalSessionExportSanitizeType0 | None | Unset = UNSET,

) -> Response[ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Export session

     Export a complete projected session transcript.

    Args:
        session_id (str):
        sanitize (ExperimentalSessionExportSanitizeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
sanitize=sanitize,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    sanitize: ExperimentalSessionExportSanitizeType0 | None | Unset = UNSET,

) -> ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Export session

     Export a complete projected session transcript.

    Args:
        session_id (str):
        sanitize (ExperimentalSessionExportSanitizeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,
sanitize=sanitize,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    sanitize: ExperimentalSessionExportSanitizeType0 | None | Unset = UNSET,

) -> Response[ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]:
    """ Export session

     Export a complete projected session transcript.

    Args:
        session_id (str):
        sanitize (ExperimentalSessionExportSanitizeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
sanitize=sanitize,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    sanitize: ExperimentalSessionExportSanitizeType0 | None | Unset = UNSET,

) -> ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded | None:
    """ Export session

     Export a complete projected session transcript.

    Args:
        session_id (str):
        sanitize (ExperimentalSessionExportSanitizeType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentalSessionExportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | UnknownErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
sanitize=sanitize,

    )).parsed
