from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_inbox_compaction_type import SessionInboxCompactionType
from ..models.session_inbox_delivery import SessionInboxDelivery
from typing import cast

if TYPE_CHECKING:
  from ..models.session_inbox_compaction_time import SessionInboxCompactionTime





T = TypeVar("T", bound="SessionInboxCompaction")



@_attrs_define
class SessionInboxCompaction:
    """ 
        Attributes:
            delivery (SessionInboxDelivery):
            id (str):
            payload (Any):
            session_id (str):
            time (SessionInboxCompactionTime):
            type_ (SessionInboxCompactionType):
     """

    delivery: SessionInboxDelivery
    id: str
    payload: Any
    session_id: str
    time: SessionInboxCompactionTime
    type_: SessionInboxCompactionType





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_inbox_compaction_time import SessionInboxCompactionTime # noqa: PLC0415
        delivery = self.delivery.value

        id = self.id

        payload = self.payload

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
        from ..models.session_inbox_compaction_time import SessionInboxCompactionTime # noqa: PLC0415
        d = dict(src_dict)
        delivery = SessionInboxDelivery(d.pop("delivery"))




        id = d.pop("id")

        payload = d.pop("payload")

        session_id = d.pop("sessionID")

        time = SessionInboxCompactionTime.from_dict(d.pop("time"))




        type_ = SessionInboxCompactionType(d.pop("type"))




        session_inbox_compaction = cls(
            delivery=delivery,
            id=id,
            payload=payload,
            session_id=session_id,
            time=time,
            type_=type_,
        )

        return session_inbox_compaction

