from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PluginUpdateBody")



@_attrs_define
class PluginUpdateBody:
    """ 
        Attributes:
            targets (list[str]):
     """

    targets: list[str]





    def to_dict(self) -> dict[str, Any]:
        targets = self.targets




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "targets": targets,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        targets = cast(list[str], d.pop("targets"))


        plugin_update_body = cls(
            targets=targets,
        )

        return plugin_update_body

