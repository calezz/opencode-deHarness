from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_diff_info_status import FileDiffInfoStatus






T = TypeVar("T", bound="FileDiffInfo")



@_attrs_define
class FileDiffInfo:
    """ 
        Attributes:
            additions (int):
            deletions (int):
            file (str):
            patch (str):
            status (FileDiffInfoStatus):
     """

    additions: int
    deletions: int
    file: str
    patch: str
    status: FileDiffInfoStatus





    def to_dict(self) -> dict[str, Any]:
        additions = self.additions

        deletions = self.deletions

        file = self.file

        patch = self.patch

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "additions": additions,
            "deletions": deletions,
            "file": file,
            "patch": patch,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additions = d.pop("additions")

        deletions = d.pop("deletions")

        file = d.pop("file")

        patch = d.pop("patch")

        status = FileDiffInfoStatus(d.pop("status"))




        file_diff_info = cls(
            additions=additions,
            deletions=deletions,
            file=file,
            patch=patch,
            status=status,
        )

        return file_diff_info

