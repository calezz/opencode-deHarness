from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PluginFeatures")



@_attrs_define
class PluginFeatures:
    """ 
        Attributes:
            rpc (bool | Unset):
            server (bool | Unset):
            tui (bool | Unset):
     """

    rpc: bool | Unset = UNSET
    server: bool | Unset = UNSET
    tui: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        rpc = self.rpc

        server = self.server

        tui = self.tui


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if rpc is not UNSET:
            field_dict["rpc"] = rpc
        if server is not UNSET:
            field_dict["server"] = server
        if tui is not UNSET:
            field_dict["tui"] = tui

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rpc = d.pop("rpc", UNSET)

        server = d.pop("server", UNSET)

        tui = d.pop("tui", UNSET)

        plugin_features = cls(
            rpc=rpc,
            server=server,
            tui=tui,
        )

        return plugin_features

