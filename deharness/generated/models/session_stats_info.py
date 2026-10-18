from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_stats_activity import SessionStatsActivity
  from ..models.session_stats_info_range import SessionStatsInfoRange
  from ..models.session_stats_model_usage import SessionStatsModelUsage
  from ..models.session_stats_tools_type_0 import SessionStatsToolsType0
  from ..models.session_stats_tools_type_1 import SessionStatsToolsType1
  from ..models.session_stats_tools_type_2 import SessionStatsToolsType2
  from ..models.token_usage_info import TokenUsageInfo





T = TypeVar("T", bound="SessionStatsInfo")



@_attrs_define
class SessionStatsInfo:
    """ 
        Attributes:
            active_days (int):
            activity (list[SessionStatsActivity]):
            cost (float):
            models (list[SessionStatsModelUsage]):
            prompts (int):
            range_ (SessionStatsInfoRange):
            sessions (int):
            steps (int):
            streak (int):
            subagents (int):
            tokens (TokenUsageInfo):
            tools (SessionStatsToolsType0 | SessionStatsToolsType1 | SessionStatsToolsType2):
     """

    active_days: int
    activity: list[SessionStatsActivity]
    cost: float
    models: list[SessionStatsModelUsage]
    prompts: int
    range_: SessionStatsInfoRange
    sessions: int
    steps: int
    streak: int
    subagents: int
    tokens: TokenUsageInfo
    tools: SessionStatsToolsType0 | SessionStatsToolsType1 | SessionStatsToolsType2





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_stats_activity import SessionStatsActivity # noqa: PLC0415
        from ..models.session_stats_info_range import SessionStatsInfoRange # noqa: PLC0415
        from ..models.session_stats_model_usage import SessionStatsModelUsage # noqa: PLC0415
        from ..models.session_stats_tools_type_0 import SessionStatsToolsType0 # noqa: PLC0415
        from ..models.session_stats_tools_type_1 import SessionStatsToolsType1 # noqa: PLC0415
        from ..models.session_stats_tools_type_2 import SessionStatsToolsType2 # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        active_days = self.active_days

        activity = []
        for activity_item_data in self.activity:
            activity_item = activity_item_data.to_dict()
            activity.append(activity_item)



        cost = self.cost

        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)



        prompts = self.prompts

        range_ = self.range_.to_dict()

        sessions = self.sessions

        steps = self.steps

        streak = self.streak

        subagents = self.subagents

        tokens = self.tokens.to_dict()

        tools: dict[str, Any]
        if isinstance(self.tools, SessionStatsToolsType0):
            tools = self.tools.to_dict()
        elif isinstance(self.tools, SessionStatsToolsType1):
            tools = self.tools.to_dict()
        else:
            tools = self.tools.to_dict()



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "activeDays": active_days,
            "activity": activity,
            "cost": cost,
            "models": models,
            "prompts": prompts,
            "range": range_,
            "sessions": sessions,
            "steps": steps,
            "streak": streak,
            "subagents": subagents,
            "tokens": tokens,
            "tools": tools,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_stats_activity import SessionStatsActivity # noqa: PLC0415
        from ..models.session_stats_info_range import SessionStatsInfoRange # noqa: PLC0415
        from ..models.session_stats_model_usage import SessionStatsModelUsage # noqa: PLC0415
        from ..models.session_stats_tools_type_0 import SessionStatsToolsType0 # noqa: PLC0415
        from ..models.session_stats_tools_type_1 import SessionStatsToolsType1 # noqa: PLC0415
        from ..models.session_stats_tools_type_2 import SessionStatsToolsType2 # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        d = dict(src_dict)
        active_days = d.pop("activeDays")

        activity = []
        _activity = d.pop("activity")
        for activity_item_data in (_activity):
            activity_item = SessionStatsActivity.from_dict(activity_item_data)



            activity.append(activity_item)


        cost = d.pop("cost")

        models = []
        _models = d.pop("models")
        for models_item_data in (_models):
            models_item = SessionStatsModelUsage.from_dict(models_item_data)



            models.append(models_item)


        prompts = d.pop("prompts")

        range_ = SessionStatsInfoRange.from_dict(d.pop("range"))




        sessions = d.pop("sessions")

        steps = d.pop("steps")

        streak = d.pop("streak")

        subagents = d.pop("subagents")

        tokens = TokenUsageInfo.from_dict(d.pop("tokens"))




        def _parse_tools(data: object) -> SessionStatsToolsType0 | SessionStatsToolsType1 | SessionStatsToolsType2:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_session_stats_tools_type_0 = SessionStatsToolsType0.from_dict(data)



                return componentsschemas_session_stats_tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_session_stats_tools_type_1 = SessionStatsToolsType1.from_dict(data)



                return componentsschemas_session_stats_tools_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_session_stats_tools_type_2 = SessionStatsToolsType2.from_dict(data)



            return componentsschemas_session_stats_tools_type_2

        tools = _parse_tools(d.pop("tools"))


        session_stats_info = cls(
            active_days=active_days,
            activity=activity,
            cost=cost,
            models=models,
            prompts=prompts,
            range_=range_,
            sessions=sessions,
            steps=steps,
            streak=streak,
            subagents=subagents,
            tokens=tokens,
            tools=tools,
        )

        return session_stats_info

