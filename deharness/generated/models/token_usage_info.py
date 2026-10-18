from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.token_usage_info_cache import TokenUsageInfoCache





T = TypeVar("T", bound="TokenUsageInfo")



@_attrs_define
class TokenUsageInfo:
    """ 
        Attributes:
            cache (TokenUsageInfoCache):
            input_ (float):
            output (float):
            reasoning (float):
     """

    cache: TokenUsageInfoCache
    input_: float
    output: float
    reasoning: float





    def to_dict(self) -> dict[str, Any]:
        from ..models.token_usage_info_cache import TokenUsageInfoCache # noqa: PLC0415
        cache = self.cache.to_dict()

        input_ = self.input_

        output = self.output

        reasoning = self.reasoning


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cache": cache,
            "input": input_,
            "output": output,
            "reasoning": reasoning,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.token_usage_info_cache import TokenUsageInfoCache # noqa: PLC0415
        d = dict(src_dict)
        cache = TokenUsageInfoCache.from_dict(d.pop("cache"))




        input_ = d.pop("input")

        output = d.pop("output")

        reasoning = d.pop("reasoning")

        token_usage_info = cls(
            cache=cache,
            input_=input_,
            output=output,
            reasoning=reasoning,
        )

        return token_usage_info

