from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ConfigWorktree")



@_attrs_define
class ConfigWorktree:
    """ 
        Attributes:
            directory (str):
     """

    directory: str





    def to_dict(self) -> dict[str, Any]:
        directory = self.directory


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "directory": directory,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directory = d.pop("directory")

        config_worktree = cls(
            directory=directory,
        )

        return config_worktree

