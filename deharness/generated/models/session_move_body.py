from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_inbox_delivery import SessionInboxDelivery
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SessionMoveBody")



@_attrs_define
class SessionMoveBody:
    """ 
        Attributes:
            directory (str):
            delivery (None | SessionInboxDelivery | Unset):
     """

    directory: str
    delivery: None | SessionInboxDelivery | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        directory = self.directory

        delivery: None | str | Unset
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        elif isinstance(self.delivery, SessionInboxDelivery):
            delivery = self.delivery.value
        else:
            delivery = self.delivery


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "directory": directory,
        })
        if delivery is not UNSET:
            field_dict["delivery"] = delivery

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        directory = d.pop("directory")

        def _parse_delivery(data: object) -> None | SessionInboxDelivery | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_type_0 = SessionInboxDelivery(data)



                return delivery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionInboxDelivery | Unset, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))


        session_move_body = cls(
            directory=directory,
            delivery=delivery,
        )

        return session_move_body

