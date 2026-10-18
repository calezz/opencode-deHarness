from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionStatsInfoRange")



@_attrs_define
class SessionStatsInfoRange:
    """ 
        Attributes:
            from_ (float):
            to (float):
     """

    from_: float
    to: float





    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "from": from_,
            "to": to,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        session_stats_info_range = cls(
            from_=from_,
            to=to,
        )

        return session_stats_info_range

