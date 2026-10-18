from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SessionMessageAssistantSnapshot")



@_attrs_define
class SessionMessageAssistantSnapshot:
    """ 
        Attributes:
            end (str | Unset):
            files (list[str] | Unset):
            start (str | Unset):
     """

    end: str | Unset = UNSET
    files: list[str] | Unset = UNSET
    start: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        end = self.end

        files: list[str] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files



        start = self.start


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if end is not UNSET:
            field_dict["end"] = end
        if files is not UNSET:
            field_dict["files"] = files
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end", UNSET)

        files = cast(list[str], d.pop("files", UNSET))


        start = d.pop("start", UNSET)

        session_message_assistant_snapshot = cls(
            end=end,
            files=files,
            start=start,
        )

        return session_message_assistant_snapshot

