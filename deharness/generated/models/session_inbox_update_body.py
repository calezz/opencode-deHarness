from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_inbox_delivery import SessionInboxDelivery






T = TypeVar("T", bound="SessionInboxUpdateBody")



@_attrs_define
class SessionInboxUpdateBody:
    """ 
        Attributes:
            delivery (SessionInboxDelivery):
     """

    delivery: SessionInboxDelivery





    def to_dict(self) -> dict[str, Any]:
        delivery = self.delivery.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "delivery": delivery,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivery = SessionInboxDelivery(d.pop("delivery"))




        session_inbox_update_body = cls(
            delivery=delivery,
        )

        return session_inbox_update_body

