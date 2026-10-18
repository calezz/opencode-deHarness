from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PersistentPtySnapshotCursor")



@_attrs_define
class PersistentPtySnapshotCursor:
    """ 
        Attributes:
            x (int):
            y (int):
     """

    x: int
    y: int





    def to_dict(self) -> dict[str, Any]:
        x = self.x

        y = self.y


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "x": x,
            "y": y,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        x = d.pop("x")

        y = d.pop("y")

        persistent_pty_snapshot_cursor = cls(
            x=x,
            y=y,
        )

        return persistent_pty_snapshot_cursor

