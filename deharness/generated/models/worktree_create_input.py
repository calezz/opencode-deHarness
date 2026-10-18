from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WorktreeCreateInput")



@_attrs_define
class WorktreeCreateInput:
    """ 
        Attributes:
            project_id (str):
            branch (str | Unset):
            directory (str | Unset):
            from_ (str | Unset):
            name (str | Unset):
     """

    project_id: str
    branch: str | Unset = UNSET
    directory: str | Unset = UNSET
    from_: str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        project_id = self.project_id

        branch = self.branch

        directory = self.directory

        from_ = self.from_

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "projectID": project_id,
        })
        if branch is not UNSET:
            field_dict["branch"] = branch
        if directory is not UNSET:
            field_dict["directory"] = directory
        if from_ is not UNSET:
            field_dict["from"] = from_
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_id = d.pop("projectID")

        branch = d.pop("branch", UNSET)

        directory = d.pop("directory", UNSET)

        from_ = d.pop("from", UNSET)

        name = d.pop("name", UNSET)

        worktree_create_input = cls(
            project_id=project_id,
            branch=branch,
            directory=directory,
            from_=from_,
            name=name,
        )

        return worktree_create_input

