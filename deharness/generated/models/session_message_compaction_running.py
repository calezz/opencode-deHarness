from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_compaction_running_reason import SessionMessageCompactionRunningReason
from ..models.session_message_compaction_running_status import SessionMessageCompactionRunningStatus
from ..models.session_message_compaction_running_type import SessionMessageCompactionRunningType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_compaction_running_metadata import SessionMessageCompactionRunningMetadata
  from ..models.session_message_compaction_running_time import SessionMessageCompactionRunningTime





T = TypeVar("T", bound="SessionMessageCompactionRunning")



@_attrs_define
class SessionMessageCompactionRunning:
    """ 
        Attributes:
            id (str):
            reason (SessionMessageCompactionRunningReason):
            recent (str):
            status (SessionMessageCompactionRunningStatus):
            summary (str):
            time (SessionMessageCompactionRunningTime):
            type_ (SessionMessageCompactionRunningType):
            metadata (SessionMessageCompactionRunningMetadata | Unset):
     """

    id: str
    reason: SessionMessageCompactionRunningReason
    recent: str
    status: SessionMessageCompactionRunningStatus
    summary: str
    time: SessionMessageCompactionRunningTime
    type_: SessionMessageCompactionRunningType
    metadata: SessionMessageCompactionRunningMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_compaction_running_metadata import SessionMessageCompactionRunningMetadata # noqa: PLC0415
        from ..models.session_message_compaction_running_time import SessionMessageCompactionRunningTime # noqa: PLC0415
        id = self.id

        reason = self.reason.value

        recent = self.recent

        status = self.status.value

        summary = self.summary

        time = self.time.to_dict()

        type_ = self.type_.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "reason": reason,
            "recent": recent,
            "status": status,
            "summary": summary,
            "time": time,
            "type": type_,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_compaction_running_metadata import SessionMessageCompactionRunningMetadata # noqa: PLC0415
        from ..models.session_message_compaction_running_time import SessionMessageCompactionRunningTime # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        reason = SessionMessageCompactionRunningReason(d.pop("reason"))




        recent = d.pop("recent")

        status = SessionMessageCompactionRunningStatus(d.pop("status"))




        summary = d.pop("summary")

        time = SessionMessageCompactionRunningTime.from_dict(d.pop("time"))




        type_ = SessionMessageCompactionRunningType(d.pop("type"))




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageCompactionRunningMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageCompactionRunningMetadata.from_dict(_metadata)




        session_message_compaction_running = cls(
            id=id,
            reason=reason,
            recent=recent,
            status=status,
            summary=summary,
            time=time,
            type_=type_,
            metadata=metadata,
        )

        return session_message_compaction_running

