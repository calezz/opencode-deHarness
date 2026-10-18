from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.plugin_state_type_0_status import PluginStateType0Status






T = TypeVar("T", bound="PluginStateType0")



@_attrs_define
class PluginStateType0:
    """ 
        Attributes:
            status (PluginStateType0Status):
     """

    status: PluginStateType0Status





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = PluginStateType0Status(d.pop("status"))




        plugin_state_type_0 = cls(
            status=status,
        )

        return plugin_state_type_0

