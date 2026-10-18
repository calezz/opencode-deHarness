from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.model_cost_tier_type import ModelCostTierType






T = TypeVar("T", bound="ModelCostTier")



@_attrs_define
class ModelCostTier:
    """ 
        Attributes:
            size (int):
            type_ (ModelCostTierType):
     """

    size: int
    type_: ModelCostTierType





    def to_dict(self) -> dict[str, Any]:
        size = self.size

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "size": size,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size = d.pop("size")

        type_ = ModelCostTierType(d.pop("type"))




        model_cost_tier = cls(
            size=size,
            type_=type_,
        )

        return model_cost_tier

