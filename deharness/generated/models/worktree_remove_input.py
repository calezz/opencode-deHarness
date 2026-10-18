from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="WorktreeRemoveInput")



@_attrs_define
class WorktreeRemoveInput:
    """ 
        Attributes:
            directory (str):
            force (bool):
            project_id (str):
     """

    directory: str
    force: bool
    project_id: str





    def to_dict(self) -> dict[str, Any]:
        directory = self.directory

        force = self.force

        project_id = self.project_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "directory": directory,
            "force": force,
            "projectID": project_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directory = d.pop("directory")

        force = d.pop("force")

        project_id = d.pop("projectID")

        worktree_remove_input = cls(
            directory=directory,
            force=force,
            project_id=project_id,
        )

        return worktree_remove_input

