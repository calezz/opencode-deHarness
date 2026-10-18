from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_compaction_failed_reason import SessionMessageCompactionFailedReason
from ..models.session_message_compaction_failed_status import SessionMessageCompactionFailedStatus
from ..models.session_message_compaction_failed_type import SessionMessageCompactionFailedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_compaction_failed_metadata import SessionMessageCompactionFailedMetadata
  from ..models.session_message_compaction_failed_time import SessionMessageCompactionFailedTime
  from ..models.session_structured_error import SessionStructuredError
  from ..models.token_usage_info import TokenUsageInfo





T = TypeVar("T", bound="SessionMessageCompactionFailed")



@_attrs_define
class SessionMessageCompactionFailed:
    """ 
        Attributes:
            error (SessionStructuredError):
            id (str):
            reason (SessionMessageCompactionFailedReason):
            status (SessionMessageCompactionFailedStatus):
            time (SessionMessageCompactionFailedTime):
            type_ (SessionMessageCompactionFailedType):
            cost (float | Unset):
            metadata (SessionMessageCompactionFailedMetadata | Unset):
            tokens (TokenUsageInfo | Unset):
     """

    error: SessionStructuredError
    id: str
    reason: SessionMessageCompactionFailedReason
    status: SessionMessageCompactionFailedStatus
    time: SessionMessageCompactionFailedTime
    type_: SessionMessageCompactionFailedType
    cost: float | Unset = UNSET
    metadata: SessionMessageCompactionFailedMetadata | Unset = UNSET
    tokens: TokenUsageInfo | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_compaction_failed_metadata import SessionMessageCompactionFailedMetadata # noqa: PLC0415
        from ..models.session_message_compaction_failed_time import SessionMessageCompactionFailedTime # noqa: PLC0415
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        error = self.error.to_dict()

        id = self.id

        reason = self.reason.value

        status = self.status.value

        time = self.time.to_dict()

        type_ = self.type_.value

        cost = self.cost

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        tokens: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = self.tokens.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "id": id,
            "reason": reason,
            "status": status,
            "time": time,
            "type": type_,
        })
        if cost is not UNSET:
            field_dict["cost"] = cost
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_compaction_failed_metadata import SessionMessageCompactionFailedMetadata # noqa: PLC0415
        from ..models.session_message_compaction_failed_time import SessionMessageCompactionFailedTime # noqa: PLC0415
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        d = dict(src_dict)
        error = SessionStructuredError.from_dict(d.pop("error"))




        id = d.pop("id")

        reason = SessionMessageCompactionFailedReason(d.pop("reason"))




        status = SessionMessageCompactionFailedStatus(d.pop("status"))




        time = SessionMessageCompactionFailedTime.from_dict(d.pop("time"))




        type_ = SessionMessageCompactionFailedType(d.pop("type"))




        cost = d.pop("cost", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageCompactionFailedMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageCompactionFailedMetadata.from_dict(_metadata)




        _tokens = d.pop("tokens", UNSET)
        tokens: TokenUsageInfo | Unset
        if isinstance(_tokens,  Unset):
            tokens = UNSET
        else:
            tokens = TokenUsageInfo.from_dict(_tokens)




        session_message_compaction_failed = cls(
            error=error,
            id=id,
            reason=reason,
            status=status,
            time=time,
            type_=type_,
            cost=cost,
            metadata=metadata,
            tokens=tokens,
        )

        return session_message_compaction_failed

