from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_structured_error_response import SessionStructuredErrorResponse





T = TypeVar("T", bound="SessionStructuredError")



@_attrs_define
class SessionStructuredError:
    """ 
        Attributes:
            message (str):
            type_ (str):
            response (SessionStructuredErrorResponse | Unset):
            status (int | Unset):
     """

    message: str
    type_: str
    response: SessionStructuredErrorResponse | Unset = UNSET
    status: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_structured_error_response import SessionStructuredErrorResponse # noqa: PLC0415
        message = self.message

        type_ = self.type_

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        status = self.status


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "message": message,
            "type": type_,
        })
        if response is not UNSET:
            field_dict["response"] = response
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_structured_error_response import SessionStructuredErrorResponse # noqa: PLC0415
        d = dict(src_dict)
        message = d.pop("message")

        type_ = d.pop("type")

        _response = d.pop("response", UNSET)
        response: SessionStructuredErrorResponse | Unset
        if isinstance(_response,  Unset):
            response = UNSET
        else:
            response = SessionStructuredErrorResponse.from_dict(_response)




        status = d.pop("status", UNSET)

        session_structured_error = cls(
            message=message,
            type_=type_,
            response=response,
            status=status,
        )

        return session_structured_error

