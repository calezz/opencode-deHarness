from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reference_git_source_type import ReferenceGitSourceType
from ..types import UNSET, Unset






T = TypeVar("T", bound="ReferenceGitSource")



@_attrs_define
class ReferenceGitSource:
    """ 
        Attributes:
            repository (str):
            type_ (ReferenceGitSourceType):
            branch (str | Unset):
     """

    repository: str
    type_: ReferenceGitSourceType
    branch: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        repository = self.repository

        type_ = self.type_.value

        branch = self.branch


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "repository": repository,
            "type": type_,
        })
        if branch is not UNSET:
            field_dict["branch"] = branch

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository = d.pop("repository")

        type_ = ReferenceGitSourceType(d.pop("type"))




        branch = d.pop("branch", UNSET)

        reference_git_source = cls(
            repository=repository,
            type_=type_,
            branch=branch,
        )

        return reference_git_source

