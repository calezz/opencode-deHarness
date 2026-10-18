from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigModelReasoningType1Budget")



@_attrs_define
class ConfigModelReasoningType1Budget:
    """ 
        Attributes:
            max_ (int | Unset):
            min_ (int | Unset):
     """

    max_: int | Unset = UNSET
    min_: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        max_ = self.max_

        min_ = self.min_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        config_model_reasoning_type_1_budget = cls(
            max_=max_,
            min_=min_,
        )

        return config_model_reasoning_type_1_budget

