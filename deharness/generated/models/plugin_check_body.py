from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PluginCheckBody")



@_attrs_define
class PluginCheckBody:
    """ 
        Attributes:
            target (None | str | Unset):
     """

    target: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        target: None | str | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target = _parse_target(d.pop("target", UNSET))


        plugin_check_body = cls(
            target=target,
        )

        return plugin_check_body

