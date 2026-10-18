from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_inbox_delivery import SessionInboxDelivery
from ..models.session_inbox_move_type import SessionInboxMoveType
from typing import cast

if TYPE_CHECKING:
  from ..models.session_inbox_move_payload import SessionInboxMovePayload
  from ..models.session_inbox_move_time import SessionInboxMoveTime





T = TypeVar("T", bound="SessionInboxMove")



@_attrs_define
class SessionInboxMove:
    """ 
        Attributes:
            delivery (SessionInboxDelivery):
            id (str):
            payload (SessionInboxMovePayload):
            session_id (str):
            time (SessionInboxMoveTime):
            type_ (SessionInboxMoveType):
     """

    delivery: SessionInboxDelivery
    id: str
    payload: SessionInboxMovePayload
    session_id: str
    time: SessionInboxMoveTime
    type_: SessionInboxMoveType





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_inbox_move_payload import SessionInboxMovePayload # noqa: PLC0415
        from ..models.session_inbox_move_time import SessionInboxMoveTime # noqa: PLC0415
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
        from ..models.session_inbox_move_payload import SessionInboxMovePayload # noqa: PLC0415
        from ..models.session_inbox_move_time import SessionInboxMoveTime # noqa: PLC0415
        d = dict(src_dict)
        delivery = SessionInboxDelivery(d.pop("delivery"))




        id = d.pop("id")

        payload = SessionInboxMovePayload.from_dict(d.pop("payload"))




        session_id = d.pop("sessionID")

        time = SessionInboxMoveTime.from_dict(d.pop("time"))




        type_ = SessionInboxMoveType(d.pop("type"))




        session_inbox_move = cls(
            delivery=delivery,
            id=id,
            payload=payload,
            session_id=session_id,
            time=time,
            type_=type_,
        )

        return session_inbox_move

