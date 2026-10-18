from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.project_not_found_error_encoded import ProjectNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...models.worktree_error_encoded import WorktreeErrorEncoded
from ...models.worktree_remove_input import WorktreeRemoveInput
from typing import cast



def _get_kwargs(
    *,
    body: WorktreeRemoveInput,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/worktree",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        def _parse_response_400(data: object) -> InvalidRequestErrorEncoded | WorktreeErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_400_type_0 = WorktreeErrorEncoded.from_dict(data)



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
        response_404 = ProjectNotFoundErrorEncoded.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WorktreeRemoveInput,

) -> Response[Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Remove worktree

     Load the project's canonical configuration and remove a saved worktree using its recorded strategy.

    Args:
        body (WorktreeRemoveInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded]
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
    body: WorktreeRemoveInput,

) -> Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Remove worktree

     Load the project's canonical configuration and remove a saved worktree using its recorded strategy.

    Args:
        body (WorktreeRemoveInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: WorktreeRemoveInput,

) -> Response[Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded]:
    """ Remove worktree

     Load the project's canonical configuration and remove a saved worktree using its recorded strategy.

    Args:
        body (WorktreeRemoveInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded]
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
    body: WorktreeRemoveInput,

) -> Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Remove worktree

     Load the project's canonical configuration and remove a saved worktree using its recorded strategy.

    Args:
        body (WorktreeRemoveInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | WorktreeErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
