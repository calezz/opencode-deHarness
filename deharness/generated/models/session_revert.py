from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.file_diff_info import FileDiffInfo





T = TypeVar("T", bound="SessionRevert")



@_attrs_define
class SessionRevert:
    """ 
        Attributes:
            message_id (str):
            files (list[FileDiffInfo] | Unset):
            part_id (str | Unset):
            snapshot (str | Unset):
     """

    message_id: str
    files: list[FileDiffInfo] | Unset = UNSET
    part_id: str | Unset = UNSET
    snapshot: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_diff_info import FileDiffInfo # noqa: PLC0415
        message_id = self.message_id

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        part_id = self.part_id

        snapshot = self.snapshot


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "messageID": message_id,
        })
        if files is not UNSET:
            field_dict["files"] = files
        if part_id is not UNSET:
            field_dict["partID"] = part_id
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_diff_info import FileDiffInfo # noqa: PLC0415
        d = dict(src_dict)
        message_id = d.pop("messageID")

        _files = d.pop("files", UNSET)
        files: list[FileDiffInfo] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FileDiffInfo.from_dict(files_item_data)



                files.append(files_item)


        part_id = d.pop("partID", UNSET)

        snapshot = d.pop("snapshot", UNSET)

        session_revert = cls(
            message_id=message_id,
            files=files,
            part_id=part_id,
            snapshot=snapshot,
        )

        return session_revert

