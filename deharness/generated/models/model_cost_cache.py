from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ModelCostCache")



@_attrs_define
class ModelCostCache:
    """ 
        Attributes:
            read (float):
            write (float):
     """

    read: float
    write: float





    def to_dict(self) -> dict[str, Any]:
        read = self.read

        write = self.write


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "read": read,
            "write": write,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read = d.pop("read")

        write = d.pop("write")

        model_cost_cache = cls(
            read=read,
            write=write,
        )

        return model_cost_cache

