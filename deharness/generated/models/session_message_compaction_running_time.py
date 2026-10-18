from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionMessageCompactionRunningTime")



@_attrs_define
class SessionMessageCompactionRunningTime:
    """ 
        Attributes:
            created (float):
     """

    created: float





    def to_dict(self) -> dict[str, Any]:
        created = self.created


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "created": created,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        session_message_compaction_running_time = cls(
            created=created,
        )

        return session_message_compaction_running_time

