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
from ...models.worktree_directory import WorktreeDirectory
from typing import cast



def _get_kwargs(
    *,
    project_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["projectID"] = project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/worktree",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_worktree_list_item_data in (_response_200):
            componentsschemas_worktree_list_item = WorktreeDirectory.from_dict(componentsschemas_worktree_list_item_data)



            response_200.append(componentsschemas_worktree_list_item)

        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,

) -> Response[InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory]]:
    """ List worktrees

     Return the project's saved worktree inventory without loading configuration or running discovery.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,

) -> InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory] | None:
    """ List worktrees

     Return the project's saved worktree inventory without loading configuration or running discovery.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory]
     """


    return sync_detailed(
        client=client,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,

) -> Response[InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory]]:
    """ List worktrees

     Return the project's saved worktree inventory without loading configuration or running discovery.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str,

) -> InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory] | None:
    """ List worktrees

     Return the project's saved worktree inventory without loading configuration or running discovery.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | ProjectNotFoundErrorEncoded | UnauthorizedErrorEncoded | list[WorktreeDirectory]
     """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,

    )).parsed
