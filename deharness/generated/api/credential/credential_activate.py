from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from typing import cast



def _get_kwargs(
    credential_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/credential/{credential_id}/activate".format(credential_id=quote(str(credential_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Activate credential

     Activate a stored integration credential.

    Args:
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        credential_id=credential_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Activate credential

     Activate a stored integration credential.

    Args:
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        credential_id=credential_id,
client=client,

    ).parsed

async def asyncio_detailed(
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Activate credential

     Activate a stored integration credential.

    Args:
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        credential_id=credential_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    credential_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Activate credential

     Activate a stored integration credential.

    Args:
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        credential_id=credential_id,
client=client,

    )).parsed
