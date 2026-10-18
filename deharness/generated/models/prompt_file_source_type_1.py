from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.prompt_file_source_type_1_type import PromptFileSourceType1Type






T = TypeVar("T", bound="PromptFileSourceType1")



@_attrs_define
class PromptFileSourceType1:
    """ 
        Attributes:
            type_ (PromptFileSourceType1Type):
            uri (str):
     """

    type_: PromptFileSourceType1Type
    uri: str





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        uri = self.uri


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "uri": uri,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = PromptFileSourceType1Type(d.pop("type"))




        uri = d.pop("uri")

        prompt_file_source_type_1 = cls(
            type_=type_,
            uri=uri,
        )

        return prompt_file_source_type_1

