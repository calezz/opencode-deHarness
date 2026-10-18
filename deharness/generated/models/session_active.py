from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_active_type import SessionActiveType






T = TypeVar("T", bound="SessionActive")



@_attrs_define
class SessionActive:
    """ 
        Attributes:
            type_ (SessionActiveType):
     """

    type_: SessionActiveType





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SessionActiveType(d.pop("type"))




        session_active = cls(
            type_=type_,
        )

        return session_active

