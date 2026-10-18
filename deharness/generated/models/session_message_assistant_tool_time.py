from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SessionMessageAssistantToolTime")



@_attrs_define
class SessionMessageAssistantToolTime:
    """ 
        Attributes:
            created (float):
            completed (float | Unset):
            ran (float | Unset):
     """

    created: float
    completed: float | Unset = UNSET
    ran: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created = self.created

        completed = self.completed

        ran = self.ran


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "created": created,
        })
        if completed is not UNSET:
            field_dict["completed"] = completed
        if ran is not UNSET:
            field_dict["ran"] = ran

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        completed = d.pop("completed", UNSET)

        ran = d.pop("ran", UNSET)

        session_message_assistant_tool_time = cls(
            created=created,
            completed=completed,
            ran=ran,
        )

        return session_message_assistant_tool_time

