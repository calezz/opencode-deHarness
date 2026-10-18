from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ConfigShellOption")



@_attrs_define
class ConfigShellOption:
    """ 
        Attributes:
            acceptable (bool):
            name (str):
            path (str):
     """

    acceptable: bool
    name: str
    path: str





    def to_dict(self) -> dict[str, Any]:
        acceptable = self.acceptable

        name = self.name

        path = self.path


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "acceptable": acceptable,
            "name": name,
            "path": path,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acceptable = d.pop("acceptable")

        name = d.pop("name")

        path = d.pop("path")

        config_shell_option = cls(
            acceptable=acceptable,
            name=name,
            path=path,
        )

        return config_shell_option

