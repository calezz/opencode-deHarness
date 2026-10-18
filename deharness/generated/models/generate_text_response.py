from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.generate_text_response_data import GenerateTextResponseData





T = TypeVar("T", bound="GenerateTextResponse")



@_attrs_define
class GenerateTextResponse:
    """ 
        Attributes:
            data (GenerateTextResponseData):
     """

    data: GenerateTextResponseData





    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_text_response_data import GenerateTextResponseData # noqa: PLC0415
        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_text_response_data import GenerateTextResponseData # noqa: PLC0415
        d = dict(src_dict)
        data = GenerateTextResponseData.from_dict(d.pop("data"))




        generate_text_response = cls(
            data=data,
        )

        return generate_text_response

