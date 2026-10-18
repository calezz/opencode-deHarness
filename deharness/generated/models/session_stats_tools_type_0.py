from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_stats_tools_type_0_mode import SessionStatsToolsType0Mode






T = TypeVar("T", bound="SessionStatsToolsType0")



@_attrs_define
class SessionStatsToolsType0:
    """ 
        Attributes:
            mode (SessionStatsToolsType0Mode):
     """

    mode: SessionStatsToolsType0Mode





    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mode": mode,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = SessionStatsToolsType0Mode(d.pop("mode"))




        session_stats_tools_type_0 = cls(
            mode=mode,
        )

        return session_stats_tools_type_0

