from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.instruction_entry_value_too_large_error_encoded_tag import InstructionEntryValueTooLargeErrorEncodedTag






T = TypeVar("T", bound="InstructionEntryValueTooLargeErrorEncoded")



@_attrs_define
class InstructionEntryValueTooLargeErrorEncoded:
    """ 
        Attributes:
            field_tag (InstructionEntryValueTooLargeErrorEncodedTag):
            actual_bytes (int):
            max_bytes (int):
            message (str):
     """

    field_tag: InstructionEntryValueTooLargeErrorEncodedTag
    actual_bytes: int
    max_bytes: int
    message: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        actual_bytes = self.actual_bytes

        max_bytes = self.max_bytes

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "actualBytes": actual_bytes,
            "maxBytes": max_bytes,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = InstructionEntryValueTooLargeErrorEncodedTag(d.pop("_tag"))




        actual_bytes = d.pop("actualBytes")

        max_bytes = d.pop("maxBytes")

        message = d.pop("message")

        instruction_entry_value_too_large_error_encoded = cls(
            field_tag=field_tag,
            actual_bytes=actual_bytes,
            max_bytes=max_bytes,
            message=message,
        )

        return instruction_entry_value_too_large_error_encoded

