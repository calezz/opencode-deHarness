from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ServerInfoCapabilitiesType0")



@_attrs_define
class ServerInfoCapabilitiesType0:
    """ 
        Attributes:
            persistent_pty (bool | None | Unset):
     """

    persistent_pty: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        persistent_pty: bool | None | Unset
        if isinstance(self.persistent_pty, Unset):
            persistent_pty = UNSET
        else:
            persistent_pty = self.persistent_pty


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if persistent_pty is not UNSET:
            field_dict["persistentPty"] = persistent_pty

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_persistent_pty(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        persistent_pty = _parse_persistent_pty(d.pop("persistentPty", UNSET))


        server_info_capabilities_type_0 = cls(
            persistent_pty=persistent_pty,
        )

        return server_info_capabilities_type_0

