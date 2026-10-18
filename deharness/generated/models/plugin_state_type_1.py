from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.plugin_state_type_1_status import PluginStateType1Status
from ..types import UNSET, Unset






T = TypeVar("T", bound="PluginStateType1")



@_attrs_define
class PluginStateType1:
    """ 
        Attributes:
            error (str):
            status (PluginStateType1Status):
            ref (str | Unset):
     """

    error: str
    status: PluginStateType1Status
    ref: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error = self.error

        status = self.status.value

        ref = self.ref


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "status": status,
        })
        if ref is not UNSET:
            field_dict["ref"] = ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        status = PluginStateType1Status(d.pop("status"))




        ref = d.pop("ref", UNSET)

        plugin_state_type_1 = cls(
            error=error,
            status=status,
            ref=ref,
        )

        return plugin_state_type_1

