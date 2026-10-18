from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_inbox_delivery import SessionInboxDelivery
from ..models.session_inbox_synthetic_type import SessionInboxSyntheticType
from typing import cast

if TYPE_CHECKING:
  from ..models.session_inbox_synthetic_payload import SessionInboxSyntheticPayload
  from ..models.session_inbox_synthetic_time import SessionInboxSyntheticTime





T = TypeVar("T", bound="SessionInboxSynthetic")



@_attrs_define
class SessionInboxSynthetic:
    """ 
        Attributes:
            delivery (SessionInboxDelivery):
            id (str):
            payload (SessionInboxSyntheticPayload):
            session_id (str):
            time (SessionInboxSyntheticTime):
            type_ (SessionInboxSyntheticType):
     """

    delivery: SessionInboxDelivery
    id: str
    payload: SessionInboxSyntheticPayload
    session_id: str
    time: SessionInboxSyntheticTime
    type_: SessionInboxSyntheticType





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_inbox_synthetic_payload import SessionInboxSyntheticPayload # noqa: PLC0415
        from ..models.session_inbox_synthetic_time import SessionInboxSyntheticTime # noqa: PLC0415
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
        from ..models.session_inbox_synthetic_payload import SessionInboxSyntheticPayload # noqa: PLC0415
        from ..models.session_inbox_synthetic_time import SessionInboxSyntheticTime # noqa: PLC0415
        d = dict(src_dict)
        delivery = SessionInboxDelivery(d.pop("delivery"))




        id = d.pop("id")

        payload = SessionInboxSyntheticPayload.from_dict(d.pop("payload"))




        session_id = d.pop("sessionID")

        time = SessionInboxSyntheticTime.from_dict(d.pop("time"))




        type_ = SessionInboxSyntheticType(d.pop("type"))




        session_inbox_synthetic = cls(
            delivery=delivery,
            id=id,
            payload=payload,
            session_id=session_id,
            time=time,
            type_=type_,
        )

        return session_inbox_synthetic

