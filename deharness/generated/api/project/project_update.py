from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.project import Project
from ...models.project_not_found_error_encoded import ProjectNotFoundErrorEncoded
from ...models.project_update_body import ProjectUpdateBody
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from typing import cast



def _get_kwargs(
    project_id: str,
    *,
    body: ProjectUpdateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/project/{project_id}".format(project_id=quote(str(project_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        def _parse_response_404(data: object) -> LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = ProjectNotFoundErrorEncoded.from_dict(data)



                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = LocationNotFoundErrorEncoded.from_dict(data)



            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectUpdateBody,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded]:
    """ Update project

     Update the project canonical directory, display metadata, and workspace commands.

    Args:
        project_id (str):
        body (ProjectUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectUpdateBody,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded | None:
    """ Update project

     Update the project canonical directory, display metadata, and workspace commands.

    Args:
        project_id (str):
        body (ProjectUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        project_id=project_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectUpdateBody,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded]:
    """ Update project

     Update the project canonical directory, display metadata, and workspace commands.

    Args:
        project_id (str):
        body (ProjectUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectUpdateBody,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded | None:
    """ Update project

     Update the project canonical directory, display metadata, and workspace commands.

    Args:
        project_id (str):
        body (ProjectUpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | ProjectNotFoundErrorEncoded | Project | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
body=body,

    )).parsed
