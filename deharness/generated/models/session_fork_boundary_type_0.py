from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_fork_boundary_type_0_type import SessionForkBoundaryType0Type






T = TypeVar("T", bound="SessionForkBoundaryType0")



@_attrs_define
class SessionForkBoundaryType0:
    """ 
        Attributes:
            message_id (str):
            type_ (SessionForkBoundaryType0Type):
     """

    message_id: str
    type_: SessionForkBoundaryType0Type





    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "messageID": message_id,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message_id = d.pop("messageID")

        type_ = SessionForkBoundaryType0Type(d.pop("type"))




        session_fork_boundary_type_0 = cls(
            message_id=message_id,
            type_=type_,
        )

        return session_fork_boundary_type_0

