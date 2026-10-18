from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pty_update_body_size import PtyUpdateBodySize





T = TypeVar("T", bound="PtyUpdateBody")



@_attrs_define
class PtyUpdateBody:
    """ 
        Attributes:
            size (PtyUpdateBodySize | Unset):
            title (str | Unset):
     """

    size: PtyUpdateBodySize | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.pty_update_body_size import PtyUpdateBodySize # noqa: PLC0415
        size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.to_dict()

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if size is not UNSET:
            field_dict["size"] = size
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pty_update_body_size import PtyUpdateBodySize # noqa: PLC0415
        d = dict(src_dict)
        _size = d.pop("size", UNSET)
        size: PtyUpdateBodySize | Unset
        if isinstance(_size,  Unset):
            size = UNSET
        else:
            size = PtyUpdateBodySize.from_dict(_size)




        title = d.pop("title", UNSET)

        pty_update_body = cls(
            size=size,
            title=title,
        )

        return pty_update_body

