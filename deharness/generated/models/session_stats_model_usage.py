from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.model_ref import ModelRef
  from ..models.token_usage_info import TokenUsageInfo





T = TypeVar("T", bound="SessionStatsModelUsage")



@_attrs_define
class SessionStatsModelUsage:
    """ 
        Attributes:
            cost (float):
            model (ModelRef):
            steps (int):
            tokens (TokenUsageInfo):
     """

    cost: float
    model: ModelRef
    steps: int
    tokens: TokenUsageInfo





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        cost = self.cost

        model = self.model.to_dict()

        steps = self.steps

        tokens = self.tokens.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cost": cost,
            "model": model,
            "steps": steps,
            "tokens": tokens,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        d = dict(src_dict)
        cost = d.pop("cost")

        model = ModelRef.from_dict(d.pop("model"))




        steps = d.pop("steps")

        tokens = TokenUsageInfo.from_dict(d.pop("tokens"))




        session_stats_model_usage = cls(
            cost=cost,
            model=model,
            steps=steps,
            tokens=tokens,
        )

        return session_stats_model_usage

