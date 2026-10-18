from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.model_cost_cache import ModelCostCache
  from ..models.model_cost_tier import ModelCostTier





T = TypeVar("T", bound="ModelCost")



@_attrs_define
class ModelCost:
    """ 
        Attributes:
            cache (ModelCostCache):
            input_ (float):
            output (float):
            tier (ModelCostTier | Unset):
     """

    cache: ModelCostCache
    input_: float
    output: float
    tier: ModelCostTier | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_cost_cache import ModelCostCache # noqa: PLC0415
        from ..models.model_cost_tier import ModelCostTier # noqa: PLC0415
        cache = self.cache.to_dict()

        input_ = self.input_

        output = self.output

        tier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cache": cache,
            "input": input_,
            "output": output,
        })
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_cost_cache import ModelCostCache # noqa: PLC0415
        from ..models.model_cost_tier import ModelCostTier # noqa: PLC0415
        d = dict(src_dict)
        cache = ModelCostCache.from_dict(d.pop("cache"))




        input_ = d.pop("input")

        output = d.pop("output")

        _tier = d.pop("tier", UNSET)
        tier: ModelCostTier | Unset
        if isinstance(_tier,  Unset):
            tier = UNSET
        else:
            tier = ModelCostTier.from_dict(_tier)




        model_cost = cls(
            cache=cache,
            input_=input_,
            output=output,
            tier=tier,
        )

        return model_cost

