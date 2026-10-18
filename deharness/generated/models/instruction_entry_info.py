from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="InstructionEntryInfo")



@_attrs_define
class InstructionEntryInfo:
    """ 
        Attributes:
            key (str): Instruction entry key (lowercase alphanumerics plus . _ -)
            value (Any): JSON value attached to the session's instructions
     """

    key: str
    value: Any





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        instruction_entry_info = cls(
            key=key,
            value=value,
        )

        return instruction_entry_info

