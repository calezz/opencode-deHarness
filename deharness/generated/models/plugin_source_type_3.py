from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.plugin_source_type_3_type import PluginSourceType3Type






T = TypeVar("T", bound="PluginSourceType3")



@_attrs_define
class PluginSourceType3:
    """ 
        Attributes:
            type_ (PluginSourceType3Type):
     """

    type_: PluginSourceType3Type





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = PluginSourceType3Type(d.pop("type"))




        plugin_source_type_3 = cls(
            type_=type_,
        )

        return plugin_source_type_3

