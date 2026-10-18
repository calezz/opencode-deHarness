from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_generate_response_data import SessionGenerateResponseData





T = TypeVar("T", bound="SessionGenerateResponse")



@_attrs_define
class SessionGenerateResponse:
    """ 
        Attributes:
            data (SessionGenerateResponseData):
     """

    data: SessionGenerateResponseData





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_generate_response_data import SessionGenerateResponseData # noqa: PLC0415
        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_generate_response_data import SessionGenerateResponseData # noqa: PLC0415
        d = dict(src_dict)
        data = SessionGenerateResponseData.from_dict(d.pop("data"))




        session_generate_response = cls(
            data=data,
        )

        return session_generate_response

