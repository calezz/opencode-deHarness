from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="WorktreeRefreshBody")



@_attrs_define
class WorktreeRefreshBody:
    """ 
        Attributes:
            project_id (str):
     """

    project_id: str





    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "projectID": project_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectID")

        worktree_refresh_body = cls(
            project_id=project_id,
        )

        return worktree_refresh_body

