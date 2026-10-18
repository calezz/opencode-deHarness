from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_model_cost_encoded_cache import ConfigModelCostEncodedCache
  from ..models.config_model_cost_encoded_tier import ConfigModelCostEncodedTier





T = TypeVar("T", bound="ConfigModelCostEncoded")



@_attrs_define
class ConfigModelCostEncoded:
    """ 
        Attributes:
            input_ (float):
            output (float):
            cache (ConfigModelCostEncodedCache | Unset):
            tier (ConfigModelCostEncodedTier | Unset):
     """

    input_: float
    output: float
    cache: ConfigModelCostEncodedCache | Unset = UNSET
    tier: ConfigModelCostEncodedTier | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_model_cost_encoded_cache import ConfigModelCostEncodedCache # noqa: PLC0415
        from ..models.config_model_cost_encoded_tier import ConfigModelCostEncodedTier # noqa: PLC0415
        input_ = self.input_

        output = self.output

        cache: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cache, Unset):
            cache = self.cache.to_dict()

        tier: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "input": input_,
            "output": output,
        })
        if cache is not UNSET:
            field_dict["cache"] = cache
        if tier is not UNSET:
            field_dict["tier"] = tier

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_model_cost_encoded_cache import ConfigModelCostEncodedCache # noqa: PLC0415
        from ..models.config_model_cost_encoded_tier import ConfigModelCostEncodedTier # noqa: PLC0415
        d = dict(src_dict)
        input_ = d.pop("input")

        output = d.pop("output")

        _cache = d.pop("cache", UNSET)
        cache: ConfigModelCostEncodedCache | Unset
        if isinstance(_cache,  Unset):
            cache = UNSET
        else:
            cache = ConfigModelCostEncodedCache.from_dict(_cache)




        _tier = d.pop("tier", UNSET)
        tier: ConfigModelCostEncodedTier | Unset
        if isinstance(_tier,  Unset):
            tier = UNSET
        else:
            tier = ConfigModelCostEncodedTier.from_dict(_tier)




        config_model_cost_encoded = cls(
            input_=input_,
            output=output,
            cache=cache,
            tier=tier,
        )

        return config_model_cost_encoded

