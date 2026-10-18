from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SessionRevertStageBody")



@_attrs_define
class SessionRevertStageBody:
    """ 
        Attributes:
            message_id (str):
            files (bool | None | Unset):
     """

    message_id: str
    files: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        files: bool | None | Unset
        if isinstance(self.files, Unset):
            files = UNSET
        else:
            files = self.files


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "messageID": message_id,
        })
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageID")

        def _parse_files(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        files = _parse_files(d.pop("files", UNSET))


        session_revert_stage_body = cls(
            message_id=message_id,
            files=files,
        )

        return session_revert_stage_body

