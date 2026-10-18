from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ConfigModelReasoningType0")



@_attrs_define
class ConfigModelReasoningType0:
    """ 
        Attributes:
            supported (bool):
     """

    supported: bool





    def to_dict(self) -> dict[str, Any]:
        supported = self.supported


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "supported": supported,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        supported = d.pop("supported")

        config_model_reasoning_type_0 = cls(
            supported=supported,
        )

        return config_model_reasoning_type_0

