from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conflict_error_encoded import ConflictErrorEncoded
from ...models.experimental_session_import_body import ExperimentalSessionImportBody
from ...models.experimental_session_import_response_200 import ExperimentalSessionImportResponse200
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from typing import cast



def _get_kwargs(
    *,
    body: ExperimentalSessionImportBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/experimental/session/import",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = ExperimentalSessionImportResponse200.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = ConflictErrorEncoded.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalSessionImportBody,

) -> Response[ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Import session

     Import a projected session transcript at the requested location. If parentID is supplied, the parent
    session must already exist; import parents before children.

    Args:
        body (ExperimentalSessionImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalSessionImportBody,

) -> ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Import session

     Import a projected session transcript at the requested location. If parentID is supplied, the parent
    session must already exist; import parents before children.

    Args:
        body (ExperimentalSessionImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalSessionImportBody,

) -> Response[ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Import session

     Import a projected session transcript at the requested location. If parentID is supplied, the parent
    session must already exist; import parents before children.

    Args:
        body (ExperimentalSessionImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExperimentalSessionImportBody,

) -> ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Import session

     Import a projected session transcript at the requested location. If parentID is supplied, the parent
    session must already exist; import parents before children.

    Args:
        body (ExperimentalSessionImportBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConflictErrorEncoded | ExperimentalSessionImportResponse200 | InvalidRequestErrorEncoded | SessionNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
