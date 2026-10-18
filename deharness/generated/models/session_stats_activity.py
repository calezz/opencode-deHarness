from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionStatsActivity")



@_attrs_define
class SessionStatsActivity:
    """ 
        Attributes:
            date (str):
            steps (int):
     """

    date: str
    steps: int





    def to_dict(self) -> dict[str, Any]:
        date = self.date

        steps = self.steps


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "date": date,
            "steps": steps,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        steps = d.pop("steps")

        session_stats_activity = cls(
            date=date,
            steps=steps,
        )

        return session_stats_activity

