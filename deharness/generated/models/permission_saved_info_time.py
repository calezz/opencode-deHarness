from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PermissionSavedInfoTime")



@_attrs_define
class PermissionSavedInfoTime:
    """ 
        Attributes:
            created (float):
            updated (float):
     """

    created: float
    updated: float





    def to_dict(self) -> dict[str, Any]:
        created = self.created

        updated = self.updated


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "created": created,
            "updated": updated,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        updated = d.pop("updated")

        permission_saved_info_time = cls(
            created=created,
            updated=updated,
        )

        return permission_saved_info_time

