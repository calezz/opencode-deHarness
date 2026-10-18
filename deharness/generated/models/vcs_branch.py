from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VcsBranch")



@_attrs_define
class VcsBranch:
    """ 
        Attributes:
            current (str | Unset):
            default (str | Unset):
     """

    current: str | Unset = UNSET
    default: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        current = self.current

        default = self.default


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if current is not UNSET:
            field_dict["current"] = current
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current = d.pop("current", UNSET)

        default = d.pop("default", UNSET)

        vcs_branch = cls(
            current=current,
            default=default,
        )

        return vcs_branch

