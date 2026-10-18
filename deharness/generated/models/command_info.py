from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CommandInfo")



@_attrs_define
class CommandInfo:
    """ 
        Attributes:
            name (str):
            description (str | Unset):
     """

    name: str
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        command_info = cls(
            name=name,
            description=description,
        )

        return command_info

