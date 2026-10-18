from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_text_content_type import ToolTextContentType






T = TypeVar("T", bound="ToolTextContent")



@_attrs_define
class ToolTextContent:
    """ 
        Attributes:
            text (str):
            type_ (ToolTextContentType):
     """

    text: str
    type_: ToolTextContentType





    def to_dict(self) -> dict[str, Any]:
        text = self.text

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        type_ = ToolTextContentType(d.pop("type"))




        tool_text_content = cls(
            text=text,
            type_=type_,
        )

        return tool_text_content

