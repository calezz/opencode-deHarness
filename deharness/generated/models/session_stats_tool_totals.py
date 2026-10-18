from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionStatsToolTotals")



@_attrs_define
class SessionStatsToolTotals:
    """ 
        Attributes:
            calls (int):
            failed (int):
            succeeded (int):
            unfinished (int):
     """

    calls: int
    failed: int
    succeeded: int
    unfinished: int





    def to_dict(self) -> dict[str, Any]:
        calls = self.calls

        failed = self.failed

        succeeded = self.succeeded

        unfinished = self.unfinished


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "calls": calls,
            "failed": failed,
            "succeeded": succeeded,
            "unfinished": unfinished,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calls = d.pop("calls")

        failed = d.pop("failed")

        succeeded = d.pop("succeeded")

        unfinished = d.pop("unfinished")

        session_stats_tool_totals = cls(
            calls=calls,
            failed=failed,
            succeeded=succeeded,
            unfinished=unfinished,
        )

        return session_stats_tool_totals

