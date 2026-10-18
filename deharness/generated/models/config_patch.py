from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ConfigPatch")



@_attrs_define
class ConfigPatch:
    """ 
        Attributes:
            shell (None | str):
     """

    shell: None | str





    def to_dict(self) -> dict[str, Any]:
        shell: None | str
        shell = self.shell


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "shell": shell,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_shell(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        shell = _parse_shell(d.pop("shell"))


        config_patch = cls(
            shell=shell,
        )

        return config_patch

