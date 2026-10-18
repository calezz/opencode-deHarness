from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.worktree_error_encoded_name import WorktreeErrorEncodedName
from ..models.worktree_error_encoded_tag import WorktreeErrorEncodedTag
from typing import cast

if TYPE_CHECKING:
  from ..models.worktree_error_encoded_data import WorktreeErrorEncodedData





T = TypeVar("T", bound="WorktreeErrorEncoded")



@_attrs_define
class WorktreeErrorEncoded:
    """ 
        Attributes:
            field_tag (WorktreeErrorEncodedTag):
            data (WorktreeErrorEncodedData):
            name (WorktreeErrorEncodedName):
     """

    field_tag: WorktreeErrorEncodedTag
    data: WorktreeErrorEncodedData
    name: WorktreeErrorEncodedName





    def to_dict(self) -> dict[str, Any]:
        from ..models.worktree_error_encoded_data import WorktreeErrorEncodedData # noqa: PLC0415
        field_tag = self.field_tag.value

        data = self.data.to_dict()

        name = self.name.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "data": data,
            "name": name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worktree_error_encoded_data import WorktreeErrorEncodedData # noqa: PLC0415
        d = dict(src_dict)
        field_tag = WorktreeErrorEncodedTag(d.pop("_tag"))




        data = WorktreeErrorEncodedData.from_dict(d.pop("data"))




        name = WorktreeErrorEncodedName(d.pop("name"))




        worktree_error_encoded = cls(
            field_tag=field_tag,
            data=data,
            name=name,
        )

        return worktree_error_encoded

