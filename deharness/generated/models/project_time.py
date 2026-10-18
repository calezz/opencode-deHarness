from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectTime")



@_attrs_define
class ProjectTime:
    """ 
        Attributes:
            active (int):
            created (int):
            updated (int):
            archived (int | Unset):
     """

    active: int
    created: int
    updated: int
    archived: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        active = self.active

        created = self.created

        updated = self.updated

        archived = self.archived


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "active": active,
            "created": created,
            "updated": updated,
        })
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        created = d.pop("created")

        updated = d.pop("updated")

        archived = d.pop("archived", UNSET)

        project_time = cls(
            active=active,
            created=created,
            updated=updated,
            archived=archived,
        )

        return project_time

