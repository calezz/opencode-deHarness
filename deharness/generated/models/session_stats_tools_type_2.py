from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_stats_tools_type_2_mode import SessionStatsToolsType2Mode
from typing import cast

if TYPE_CHECKING:
  from ..models.session_stats_tool_totals import SessionStatsToolTotals
  from ..models.session_stats_tool_usage import SessionStatsToolUsage





T = TypeVar("T", bound="SessionStatsToolsType2")



@_attrs_define
class SessionStatsToolsType2:
    """ 
        Attributes:
            mode (SessionStatsToolsType2Mode):
            totals (SessionStatsToolTotals):
            usage (list[SessionStatsToolUsage]):
     """

    mode: SessionStatsToolsType2Mode
    totals: SessionStatsToolTotals
    usage: list[SessionStatsToolUsage]





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_stats_tool_totals import SessionStatsToolTotals # noqa: PLC0415
        from ..models.session_stats_tool_usage import SessionStatsToolUsage # noqa: PLC0415
        mode = self.mode.value

        totals = self.totals.to_dict()

        usage = []
        for usage_item_data in self.usage:
            usage_item = usage_item_data.to_dict()
            usage.append(usage_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mode": mode,
            "totals": totals,
            "usage": usage,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_stats_tool_totals import SessionStatsToolTotals # noqa: PLC0415
        from ..models.session_stats_tool_usage import SessionStatsToolUsage # noqa: PLC0415
        d = dict(src_dict)
        mode = SessionStatsToolsType2Mode(d.pop("mode"))




        totals = SessionStatsToolTotals.from_dict(d.pop("totals"))




        usage = []
        _usage = d.pop("usage")
        for usage_item_data in (_usage):
            usage_item = SessionStatsToolUsage.from_dict(usage_item_data)



            usage.append(usage_item)


        session_stats_tools_type_2 = cls(
            mode=mode,
            totals=totals,
            usage=usage,
        )

        return session_stats_tools_type_2

