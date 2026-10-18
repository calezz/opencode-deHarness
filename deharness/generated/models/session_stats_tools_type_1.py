from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_stats_tools_type_1_mode import SessionStatsToolsType1Mode
from typing import cast

if TYPE_CHECKING:
  from ..models.session_stats_tool_totals import SessionStatsToolTotals





T = TypeVar("T", bound="SessionStatsToolsType1")



@_attrs_define
class SessionStatsToolsType1:
    """ 
        Attributes:
            mode (SessionStatsToolsType1Mode):
            totals (SessionStatsToolTotals):
     """

    mode: SessionStatsToolsType1Mode
    totals: SessionStatsToolTotals





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_stats_tool_totals import SessionStatsToolTotals # noqa: PLC0415
        mode = self.mode.value

        totals = self.totals.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mode": mode,
            "totals": totals,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_stats_tool_totals import SessionStatsToolTotals # noqa: PLC0415
        d = dict(src_dict)
        mode = SessionStatsToolsType1Mode(d.pop("mode"))




        totals = SessionStatsToolTotals.from_dict(d.pop("totals"))




        session_stats_tools_type_1 = cls(
            mode=mode,
            totals=totals,
        )

        return session_stats_tools_type_1

