from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigInfoEncodedToolOutput")



@_attrs_define
class ConfigInfoEncodedToolOutput:
    """ 
        Attributes:
            max_bytes (int | Unset):
            max_lines (int | Unset):
     """

    max_bytes: int | Unset = UNSET
    max_lines: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        max_bytes = self.max_bytes

        max_lines = self.max_lines


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if max_bytes is not UNSET:
            field_dict["max_bytes"] = max_bytes
        if max_lines is not UNSET:
            field_dict["max_lines"] = max_lines

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_bytes = d.pop("max_bytes", UNSET)

        max_lines = d.pop("max_lines", UNSET)

        config_info_encoded_tool_output = cls(
            max_bytes=max_bytes,
            max_lines=max_lines,
        )

        return config_info_encoded_tool_output

