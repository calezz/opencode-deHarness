from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PtyUpdateBodySize")



@_attrs_define
class PtyUpdateBodySize:
    """ 
        Attributes:
            cols (int):
            rows (int):
     """

    cols: int
    rows: int





    def to_dict(self) -> dict[str, Any]:
        cols = self.cols

        rows = self.rows


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cols": cols,
            "rows": rows,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cols = d.pop("cols")

        rows = d.pop("rows")

        pty_update_body_size = cls(
            cols=cols,
            rows=rows,
        )

        return pty_update_body_size

