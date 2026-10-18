from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ModelInfoTime")



@_attrs_define
class ModelInfoTime:
    """ 
        Attributes:
            released (float):
     """

    released: float





    def to_dict(self) -> dict[str, Any]:
        released = self.released


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "released": released,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        released = d.pop("released")

        model_info_time = cls(
            released=released,
        )

        return model_info_time

