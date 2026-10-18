from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigModelCostEncodedCache")



@_attrs_define
class ConfigModelCostEncodedCache:
    """ 
        Attributes:
            read (float | Unset):
            write (float | Unset):
     """

    read: float | Unset = UNSET
    write: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        read = self.read

        write = self.write


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if read is not UNSET:
            field_dict["read"] = read
        if write is not UNSET:
            field_dict["write"] = write

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read = d.pop("read", UNSET)

        write = d.pop("write", UNSET)

        config_model_cost_encoded_cache = cls(
            read=read,
            write=write,
        )

        return config_model_cost_encoded_cache

