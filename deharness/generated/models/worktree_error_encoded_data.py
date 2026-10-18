from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WorktreeErrorEncodedData")



@_attrs_define
class WorktreeErrorEncodedData:
    """ 
        Attributes:
            message (str):
            force_required (bool | None | Unset):
     """

    message: str
    force_required: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        force_required: bool | None | Unset
        if isinstance(self.force_required, Unset):
            force_required = UNSET
        else:
            force_required = self.force_required


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "message": message,
        })
        if force_required is not UNSET:
            field_dict["forceRequired"] = force_required

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        def _parse_force_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_required = _parse_force_required(d.pop("forceRequired", UNSET))


        worktree_error_encoded_data = cls(
            message=message,
            force_required=force_required,
        )

        return worktree_error_encoded_data

