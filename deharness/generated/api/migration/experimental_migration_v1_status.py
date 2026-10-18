from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.experimental_migration_v1_status_response_200_type_0 import ExperimentalMigrationV1StatusResponse200Type0
from ...models.experimental_migration_v1_status_response_200_type_1 import ExperimentalMigrationV1StatusResponse200Type1
from ...models.experimental_migration_v1_status_response_200_type_2 import ExperimentalMigrationV1StatusResponse200Type2
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/experimental/migration/v1",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ExperimentalMigrationV1StatusResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = ExperimentalMigrationV1StatusResponse200Type1.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = ExperimentalMigrationV1StatusResponse200Type2.from_dict(data)



            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Get V1 migration status

     Return the progress of the V1 to V2 session history migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Get V1 migration status

     Return the progress of the V1 to V2 session history migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Get V1 migration status

     Return the progress of the V1 to V2 session history migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Get V1 migration status

     Return the progress of the V1 to V2 session history migration.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExperimentalMigrationV1StatusResponse200Type0 | ExperimentalMigrationV1StatusResponse200Type1 | ExperimentalMigrationV1StatusResponse200Type2 | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
