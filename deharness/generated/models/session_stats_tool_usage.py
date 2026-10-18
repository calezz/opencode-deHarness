from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SessionStatsToolUsage")



@_attrs_define
class SessionStatsToolUsage:
    """ 
        Attributes:
            calls (int):
            failed (int):
            name (str):
            succeeded (int):
            unfinished (int):
            duration_p50 (float | Unset):
     """

    calls: int
    failed: int
    name: str
    succeeded: int
    unfinished: int
    duration_p50: float | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        calls = self.calls

        failed = self.failed

        name = self.name

        succeeded = self.succeeded

        unfinished = self.unfinished

        duration_p50 = self.duration_p50


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "calls": calls,
            "failed": failed,
            "name": name,
            "succeeded": succeeded,
            "unfinished": unfinished,
        })
        if duration_p50 is not UNSET:
            field_dict["durationP50"] = duration_p50

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calls = d.pop("calls")

        failed = d.pop("failed")

        name = d.pop("name")

        succeeded = d.pop("succeeded")

        unfinished = d.pop("unfinished")

        duration_p50 = d.pop("durationP50", UNSET)

        session_stats_tool_usage = cls(
            calls=calls,
            failed=failed,
            name=name,
            succeeded=succeeded,
            unfinished=unfinished,
            duration_p50=duration_p50,
        )

        return session_stats_tool_usage

