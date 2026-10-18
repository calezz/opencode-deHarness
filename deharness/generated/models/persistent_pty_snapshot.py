from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.persistent_pty_info import PersistentPtyInfo
  from ..models.persistent_pty_snapshot_cursor import PersistentPtySnapshotCursor





T = TypeVar("T", bound="PersistentPtySnapshot")



@_attrs_define
class PersistentPtySnapshot:
    """ 
        Attributes:
            checkpoint (str):
            cursor (PersistentPtySnapshotCursor):
            info (PersistentPtyInfo):
            text (str):
     """

    checkpoint: str
    cursor: PersistentPtySnapshotCursor
    info: PersistentPtyInfo
    text: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.persistent_pty_info import PersistentPtyInfo # noqa: PLC0415
        from ..models.persistent_pty_snapshot_cursor import PersistentPtySnapshotCursor # noqa: PLC0415
        checkpoint = self.checkpoint

        cursor = self.cursor.to_dict()

        info = self.info.to_dict()

        text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "checkpoint": checkpoint,
            "cursor": cursor,
            "info": info,
            "text": text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persistent_pty_info import PersistentPtyInfo # noqa: PLC0415
        from ..models.persistent_pty_snapshot_cursor import PersistentPtySnapshotCursor # noqa: PLC0415
        d = dict(src_dict)
        checkpoint = d.pop("checkpoint")

        cursor = PersistentPtySnapshotCursor.from_dict(d.pop("cursor"))




        info = PersistentPtyInfo.from_dict(d.pop("info"))




        text = d.pop("text")

        persistent_pty_snapshot = cls(
            checkpoint=checkpoint,
            cursor=cursor,
            info=info,
            text=text,
        )

        return persistent_pty_snapshot

