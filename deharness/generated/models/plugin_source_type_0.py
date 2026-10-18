from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.plugin_source_type_0_type import PluginSourceType0Type






T = TypeVar("T", bound="PluginSourceType0")



@_attrs_define
class PluginSourceType0:
    """ 
        Attributes:
            type_ (PluginSourceType0Type):
     """

    type_: PluginSourceType0Type





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
        type_ = PluginSourceType0Type(d.pop("type"))




        plugin_source_type_0 = cls(
            type_=type_,
        )

        return plugin_source_type_0

