from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.form_already_settled_error_encoded import FormAlreadySettledErrorEncoded
from ...models.form_not_found_error_encoded import FormNotFoundErrorEncoded
from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    form_id: str,
    *,
    message: None | str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_message: None | str | Unset
    if isinstance(message, Unset):
        json_message = UNSET
    else:
        json_message = message
    params["message"] = json_message


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/session/{session_id}/form/{form_id}".format(session_id=quote(str(session_id), safe=""),form_id=quote(str(form_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        def _parse_response_404(data: object) -> FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = SessionNotFoundErrorEncoded.from_dict(data)



                return response_404_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_1 = FormNotFoundErrorEncoded.from_dict(data)



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
        response_409 = FormAlreadySettledErrorEncoded.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient | Client,
    message: None | str | Unset = UNSET,

) -> Response[Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Cancel form

     Cancel a pending form, optionally telling the asker why it was not answered.

    Args:
        session_id (str):
        form_id (str):
        message (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
form_id=form_id,
message=message,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient | Client,
    message: None | str | Unset = UNSET,

) -> Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Cancel form

     Cancel a pending form, optionally telling the asker why it was not answered.

    Args:
        session_id (str):
        form_id (str):
        message (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
form_id=form_id,
client=client,
message=message,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient | Client,
    message: None | str | Unset = UNSET,

) -> Response[Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]:
    """ Cancel form

     Cancel a pending form, optionally telling the asker why it was not answered.

    Args:
        session_id (str):
        form_id (str):
        message (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
form_id=form_id,
message=message,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    form_id: str,
    *,
    client: AuthenticatedClient | Client,
    message: None | str | Unset = UNSET,

) -> Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded | None:
    """ Cancel form

     Cancel a pending form, optionally telling the asker why it was not answered.

    Args:
        session_id (str):
        form_id (str):
        message (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FormAlreadySettledErrorEncoded | FormNotFoundErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | InvalidRequestErrorEncoded | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
form_id=form_id,
client=client,
message=message,

    )).parsed
