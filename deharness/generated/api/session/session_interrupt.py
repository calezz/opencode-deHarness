from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invalid_request_error_encoded import InvalidRequestErrorEncoded
from ...models.location_not_found_error_encoded import LocationNotFoundErrorEncoded
from ...models.session_interrupt_response import SessionInterruptResponse
from ...models.session_interrupt_resume_type_0 import SessionInterruptResumeType0
from ...models.session_not_found_error_encoded import SessionNotFoundErrorEncoded
from ...models.unauthorized_error_encoded import UnauthorizedErrorEncoded
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    resume: None | SessionInterruptResumeType0 | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_resume: None | str | Unset
    if isinstance(resume, Unset):
        json_resume = UNSET
    elif isinstance(resume, SessionInterruptResumeType0):
        json_resume = resume.value
    else:
        json_resume = resume
    params["resume"] = json_resume


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/session/{session_id}/interrupt".format(session_id=quote(str(session_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded | None:
    if response.status_code == 200:
        response_200 = SessionInterruptResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InvalidRequestErrorEncoded.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UnauthorizedErrorEncoded.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        def _parse_response_404(data: object) -> LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = SessionNotFoundErrorEncoded.from_dict(data)



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded]:
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
    resume: None | SessionInterruptResumeType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded]:
    """ Interrupt session execution

     Interrupt active execution owned by this OpenCode process. Returns interrupted=true when an active
    execution was interrupted and false for the idle no-op. When resume=true, execution resumes pending
    steering input and next-in-line control items (manual compaction, moves) while queued prompts remain
    parked.

    Args:
        session_id (str):
        resume (None | SessionInterruptResumeType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
resume=resume,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    resume: None | SessionInterruptResumeType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded | None:
    """ Interrupt session execution

     Interrupt active execution owned by this OpenCode process. Returns interrupted=true when an active
    execution was interrupted and false for the idle no-op. When resume=true, execution resumes pending
    steering input and next-in-line control items (manual compaction, moves) while queued prompts remain
    parked.

    Args:
        session_id (str):
        resume (None | SessionInterruptResumeType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded
     """


    return sync_detailed(
        session_id=session_id,
client=client,
resume=resume,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    resume: None | SessionInterruptResumeType0 | Unset = UNSET,

) -> Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded]:
    """ Interrupt session execution

     Interrupt active execution owned by this OpenCode process. Returns interrupted=true when an active
    execution was interrupted and false for the idle no-op. When resume=true, execution resumes pending
    steering input and next-in-line control items (manual compaction, moves) while queued prompts remain
    parked.

    Args:
        session_id (str):
        resume (None | SessionInterruptResumeType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
resume=resume,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    resume: None | SessionInterruptResumeType0 | Unset = UNSET,

) -> InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded | None:
    """ Interrupt session execution

     Interrupt active execution owned by this OpenCode process. Returns interrupted=true when an active
    execution was interrupted and false for the idle no-op. When resume=true, execution resumes pending
    steering input and next-in-line control items (manual compaction, moves) while queued prompts remain
    parked.

    Args:
        session_id (str):
        resume (None | SessionInterruptResumeType0 | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InvalidRequestErrorEncoded | LocationNotFoundErrorEncoded | SessionNotFoundErrorEncoded | SessionInterruptResponse | UnauthorizedErrorEncoded
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
resume=resume,

    )).parsed
