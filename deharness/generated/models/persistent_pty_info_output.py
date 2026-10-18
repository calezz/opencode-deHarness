from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PersistentPtyInfoOutput")



@_attrs_define
class PersistentPtyInfoOutput:
    """ 
        Attributes:
            head (int):
            tail (int):
     """

    head: int
    tail: int





    def to_dict(self) -> dict[str, Any]:
        head = self.head

        tail = self.tail


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "head": head,
            "tail": tail,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        head = d.pop("head")

        tail = d.pop("tail")

        persistent_pty_info_output = cls(
            head=head,
            tail=tail,
        )

        return persistent_pty_info_output

