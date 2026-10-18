from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WorktreeDirectory")



@_attrs_define
class WorktreeDirectory:
    """ 
        Attributes:
            directory (str):
            strategy (str | Unset):
     """

    directory: str
    strategy: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        directory = self.directory

        strategy = self.strategy


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "directory": directory,
        })
        if strategy is not UNSET:
            field_dict["strategy"] = strategy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directory = d.pop("directory")

        strategy = d.pop("strategy", UNSET)

        worktree_directory = cls(
            directory=directory,
            strategy=strategy,
        )

        return worktree_directory

