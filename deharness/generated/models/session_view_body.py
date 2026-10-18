from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionViewBody")



@_attrs_define
class SessionViewBody:
    """ 
        Attributes:
            idle (float):
     """

    idle: float





    def to_dict(self) -> dict[str, Any]:
        idle = self.idle


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "idle": idle,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idle = d.pop("idle")

        session_view_body = cls(
            idle=idle,
        )

        return session_view_body

