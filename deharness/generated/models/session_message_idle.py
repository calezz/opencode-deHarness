from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_idle_outcome import SessionMessageIdleOutcome
from ..models.session_message_idle_type import SessionMessageIdleType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_idle_metadata import SessionMessageIdleMetadata
  from ..models.session_message_idle_time import SessionMessageIdleTime
  from ..models.session_structured_error import SessionStructuredError





T = TypeVar("T", bound="SessionMessageIdle")



@_attrs_define
class SessionMessageIdle:
    """ 
        Attributes:
            id (str):
            outcome (SessionMessageIdleOutcome):
            time (SessionMessageIdleTime):
            type_ (SessionMessageIdleType):
            error (SessionStructuredError | Unset):
            metadata (SessionMessageIdleMetadata | Unset):
     """

    id: str
    outcome: SessionMessageIdleOutcome
    time: SessionMessageIdleTime
    type_: SessionMessageIdleType
    error: SessionStructuredError | Unset = UNSET
    metadata: SessionMessageIdleMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_idle_metadata import SessionMessageIdleMetadata # noqa: PLC0415
        from ..models.session_message_idle_time import SessionMessageIdleTime # noqa: PLC0415
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        id = self.id

        outcome = self.outcome.value

        time = self.time.to_dict()

        type_ = self.type_.value

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "outcome": outcome,
            "time": time,
            "type": type_,
        })
        if error is not UNSET:
            field_dict["error"] = error
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_idle_metadata import SessionMessageIdleMetadata # noqa: PLC0415
        from ..models.session_message_idle_time import SessionMessageIdleTime # noqa: PLC0415
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        outcome = SessionMessageIdleOutcome(d.pop("outcome"))




        time = SessionMessageIdleTime.from_dict(d.pop("time"))




        type_ = SessionMessageIdleType(d.pop("type"))




        _error = d.pop("error", UNSET)
        error: SessionStructuredError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = SessionStructuredError.from_dict(_error)




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageIdleMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageIdleMetadata.from_dict(_metadata)




        session_message_idle = cls(
            id=id,
            outcome=outcome,
            time=time,
            type_=type_,
            error=error,
            metadata=metadata,
        )

        return session_message_idle

