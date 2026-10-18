from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.plugin_source_type_2_type import PluginSourceType2Type






T = TypeVar("T", bound="PluginSourceType2")



@_attrs_define
class PluginSourceType2:
    """ 
        Attributes:
            path (str):
            type_ (PluginSourceType2Type):
     """

    path: str
    type_: PluginSourceType2Type





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "path": path,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        type_ = PluginSourceType2Type(d.pop("type"))




        plugin_source_type_2 = cls(
            path=path,
            type_=type_,
        )

        return plugin_source_type_2

