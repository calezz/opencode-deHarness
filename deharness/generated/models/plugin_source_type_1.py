from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.plugin_source_type_1_type import PluginSourceType1Type
from ..types import UNSET, Unset






T = TypeVar("T", bound="PluginSourceType1")



@_attrs_define
class PluginSourceType1:
    """ 
        Attributes:
            target (str):
            type_ (PluginSourceType1Type):
            outdated (bool | Unset):
            updating (bool | Unset):
            version (str | Unset):
     """

    target: str
    type_: PluginSourceType1Type
    outdated: bool | Unset = UNSET
    updating: bool | Unset = UNSET
    version: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        target = self.target

        type_ = self.type_.value

        outdated = self.outdated

        updating = self.updating

        version = self.version


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "target": target,
            "type": type_,
        })
        if outdated is not UNSET:
            field_dict["outdated"] = outdated
        if updating is not UNSET:
            field_dict["updating"] = updating
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target = d.pop("target")

        type_ = PluginSourceType1Type(d.pop("type"))




        outdated = d.pop("outdated", UNSET)

        updating = d.pop("updating", UNSET)

        version = d.pop("version", UNSET)

        plugin_source_type_1 = cls(
            target=target,
            type_=type_,
            outdated=outdated,
            updating=updating,
            version=version,
        )

        return plugin_source_type_1

