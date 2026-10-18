from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_inbox_delivery import SessionInboxDelivery
from ..models.session_inbox_user_type import SessionInboxUserType
from typing import cast

if TYPE_CHECKING:
  from ..models.session_inbox_user_payload import SessionInboxUserPayload
  from ..models.session_inbox_user_time import SessionInboxUserTime





T = TypeVar("T", bound="SessionInboxUser")



@_attrs_define
class SessionInboxUser:
    """ 
        Attributes:
            delivery (SessionInboxDelivery):
            id (str):
            payload (SessionInboxUserPayload):
            session_id (str):
            time (SessionInboxUserTime):
            type_ (SessionInboxUserType):
     """

    delivery: SessionInboxDelivery
    id: str
    payload: SessionInboxUserPayload
    session_id: str
    time: SessionInboxUserTime
    type_: SessionInboxUserType





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_inbox_user_payload import SessionInboxUserPayload # noqa: PLC0415
        from ..models.session_inbox_user_time import SessionInboxUserTime # noqa: PLC0415
        delivery = self.delivery.value

        id = self.id

        payload = self.payload.to_dict()

        session_id = self.session_id

        time = self.time.to_dict()

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "delivery": delivery,
            "id": id,
            "payload": payload,
            "sessionID": session_id,
            "time": time,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_inbox_user_payload import SessionInboxUserPayload # noqa: PLC0415
        from ..models.session_inbox_user_time import SessionInboxUserTime # noqa: PLC0415
        d = dict(src_dict)
        delivery = SessionInboxDelivery(d.pop("delivery"))




        id = d.pop("id")

        payload = SessionInboxUserPayload.from_dict(d.pop("payload"))




        session_id = d.pop("sessionID")

        time = SessionInboxUserTime.from_dict(d.pop("time"))




        type_ = SessionInboxUserType(d.pop("type"))




        session_inbox_user = cls(
            delivery=delivery,
            id=id,
            payload=payload,
            session_id=session_id,
            time=time,
            type_=type_,
        )

        return session_inbox_user

