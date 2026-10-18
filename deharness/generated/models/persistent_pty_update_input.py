from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.persistent_pty_update_input_size import PersistentPtyUpdateInputSize





T = TypeVar("T", bound="PersistentPtyUpdateInput")



@_attrs_define
class PersistentPtyUpdateInput:
    """ 
        Attributes:
            size (PersistentPtyUpdateInputSize):
            attachment_id (str | Unset):
     """

    size: PersistentPtyUpdateInputSize
    attachment_id: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.persistent_pty_update_input_size import PersistentPtyUpdateInputSize # noqa: PLC0415
        size = self.size.to_dict()

        attachment_id = self.attachment_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "size": size,
        })
        if attachment_id is not UNSET:
            field_dict["attachmentID"] = attachment_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.persistent_pty_update_input_size import PersistentPtyUpdateInputSize # noqa: PLC0415
        d = dict(src_dict)
        size = PersistentPtyUpdateInputSize.from_dict(d.pop("size"))




        attachment_id = d.pop("attachmentID", UNSET)

        persistent_pty_update_input = cls(
            size=size,
            attachment_id=attachment_id,
        )

        return persistent_pty_update_input

