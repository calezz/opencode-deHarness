from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ShellInfoTime")



@_attrs_define
class ShellInfoTime:
    """ 
        Attributes:
            started (float): Start time in milliseconds since the Unix epoch
            completed (float | Unset):
     """

    started: float
    completed: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        started = self.started

        completed = self.completed


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "started": started,
        })
        if completed is not UNSET:
            field_dict["completed"] = completed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        started = d.pop("started")

        completed = d.pop("completed", UNSET)

        shell_info_time = cls(
            started=started,
            completed=completed,
        )

        return shell_info_time

