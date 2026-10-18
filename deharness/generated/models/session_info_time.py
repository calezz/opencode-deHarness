from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SessionInfoTime")



@_attrs_define
class SessionInfoTime:
    """ 
        Attributes:
            created (float):
            updated (float):
            archived (float | Unset):
            idle (float | Unset):
            viewed (float | Unset):
     """

    created: float
    updated: float
    archived: float | Unset = UNSET
    idle: float | Unset = UNSET
    viewed: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        created = self.created

        updated = self.updated

        archived = self.archived

        idle = self.idle

        viewed = self.viewed


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "created": created,
            "updated": updated,
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if idle is not UNSET:
            field_dict["idle"] = idle
        if viewed is not UNSET:
            field_dict["viewed"] = viewed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        updated = d.pop("updated")

        archived = d.pop("archived", UNSET)

        idle = d.pop("idle", UNSET)

        viewed = d.pop("viewed", UNSET)

        session_info_time = cls(
            created=created,
            updated=updated,
            archived=archived,
            idle=idle,
            viewed=viewed,
        )

        return session_info_time

