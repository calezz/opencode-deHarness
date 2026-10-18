from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.persistent_pty_read_result_screen_cursor import PersistentPtyReadResultScreenCursor





T = TypeVar("T", bound="PersistentPtyReadResultScreen")



@_attrs_define
class PersistentPtyReadResultScreen:
    """ 
        Attributes:
            cols (int):
            cursor (PersistentPtyReadResultScreenCursor):
            rows (int):
            text (str):
     """

    cols: int
    cursor: PersistentPtyReadResultScreenCursor
    rows: int
    text: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.persistent_pty_read_result_screen_cursor import PersistentPtyReadResultScreenCursor # noqa: PLC0415
        cols = self.cols

        cursor = self.cursor.to_dict()

        rows = self.rows

        text = self.text


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cols": cols,
            "cursor": cursor,
            "rows": rows,
            "text": text,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persistent_pty_read_result_screen_cursor import PersistentPtyReadResultScreenCursor # noqa: PLC0415
        d = dict(src_dict)
        cols = d.pop("cols")

        cursor = PersistentPtyReadResultScreenCursor.from_dict(d.pop("cursor"))




        rows = d.pop("rows")

        text = d.pop("text")

        persistent_pty_read_result_screen = cls(
            cols=cols,
            cursor=cursor,
            rows=rows,
            text=text,
        )

        return persistent_pty_read_result_screen

