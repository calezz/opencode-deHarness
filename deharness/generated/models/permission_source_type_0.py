from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_source_type_0_type import PermissionSourceType0Type






T = TypeVar("T", bound="PermissionSourceType0")



@_attrs_define
class PermissionSourceType0:
    """ 
        Attributes:
            id (str):
            message_id (str):
            type_ (PermissionSourceType0Type):
     """

    id: str
    message_id: str
    type_: PermissionSourceType0Type





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        message_id = self.message_id

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "messageID": message_id,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        message_id = d.pop("messageID")

        type_ = PermissionSourceType0Type(d.pop("type"))




        permission_source_type_0 = cls(
            id=id,
            message_id=message_id,
            type_=type_,
        )

        return permission_source_type_0

