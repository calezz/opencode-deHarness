from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionInterruptResponse")



@_attrs_define
class SessionInterruptResponse:
    """ 
        Attributes:
            interrupted (bool): Whether an active execution owned by this OpenCode process was interrupted.
     """

    interrupted: bool





    def to_dict(self) -> dict[str, Any]:
        interrupted = self.interrupted


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "interrupted": interrupted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interrupted = d.pop("interrupted")

        session_interrupt_response = cls(
            interrupted=interrupted,
        )

        return session_interrupt_response

