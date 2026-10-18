from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigReferenceGitEncoded")



@_attrs_define
class ConfigReferenceGitEncoded:
    """ 
        Attributes:
            repository (str):
            branch (str | Unset):
            description (str | Unset):
            hidden (bool | Unset):
     """

    repository: str
    branch: str | Unset = UNSET
    description: str | Unset = UNSET
    hidden: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        repository = self.repository

        branch = self.branch

        description = self.description

        hidden = self.hidden


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "repository": repository,
        })
        if branch is not UNSET:
            field_dict["branch"] = branch
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository = d.pop("repository")

        branch = d.pop("branch", UNSET)

        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        config_reference_git_encoded = cls(
            repository=repository,
            branch=branch,
            description=description,
            hidden=hidden,
        )

        return config_reference_git_encoded

