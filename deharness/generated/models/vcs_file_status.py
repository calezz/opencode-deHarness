from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vcs_file_status_status import VcsFileStatusStatus






T = TypeVar("T", bound="VcsFileStatus")



@_attrs_define
class VcsFileStatus:
    """ 
        Attributes:
            additions (int):
            deletions (int):
            file (str):
            status (VcsFileStatusStatus):
     """

    additions: int
    deletions: int
    file: str
    status: VcsFileStatusStatus





    def to_dict(self) -> dict[str, Any]:
        additions = self.additions

        deletions = self.deletions

        file = self.file

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "additions": additions,
            "deletions": deletions,
            "file": file,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additions = d.pop("additions")

        deletions = d.pop("deletions")

        file = d.pop("file")

        status = VcsFileStatusStatus(d.pop("status"))




        vcs_file_status = cls(
            additions=additions,
            deletions=deletions,
            file=file,
            status=status,
        )

        return vcs_file_status

