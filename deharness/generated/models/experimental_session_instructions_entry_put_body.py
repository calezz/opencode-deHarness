from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ExperimentalSessionInstructionsEntryPutBody")



@_attrs_define
class ExperimentalSessionInstructionsEntryPutBody:
    """ 
        Attributes:
            value (Any):
     """

    value: Any





    def to_dict(self) -> dict[str, Any]:
        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        experimental_session_instructions_entry_put_body = cls(
            value=value,
        )

        return experimental_session_instructions_entry_put_body

