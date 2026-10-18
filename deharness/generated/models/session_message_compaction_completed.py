from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_compaction_completed_reason import SessionMessageCompactionCompletedReason
from ..models.session_message_compaction_completed_status import SessionMessageCompactionCompletedStatus
from ..models.session_message_compaction_completed_type import SessionMessageCompactionCompletedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.model_ref import ModelRef
  from ..models.session_message_compaction_completed_metadata import SessionMessageCompactionCompletedMetadata
  from ..models.session_message_compaction_completed_time import SessionMessageCompactionCompletedTime
  from ..models.session_message_provider_state_5 import SessionMessageProviderState5
  from ..models.session_provider_context import SessionProviderContext
  from ..models.token_usage_info import TokenUsageInfo





T = TypeVar("T", bound="SessionMessageCompactionCompleted")



@_attrs_define
class SessionMessageCompactionCompleted:
    """ 
        Attributes:
            id (str):
            reason (SessionMessageCompactionCompletedReason):
            recent (str):
            status (SessionMessageCompactionCompletedStatus):
            summary (str):
            time (SessionMessageCompactionCompletedTime):
            type_ (SessionMessageCompactionCompletedType):
            cost (float | Unset):
            metadata (SessionMessageCompactionCompletedMetadata | Unset):
            model (ModelRef | Unset):
            provider_context (SessionProviderContext | Unset):
            provider_state (SessionMessageProviderState5 | Unset):
            tokens (TokenUsageInfo | Unset):
     """

    id: str
    reason: SessionMessageCompactionCompletedReason
    recent: str
    status: SessionMessageCompactionCompletedStatus
    summary: str
    time: SessionMessageCompactionCompletedTime
    type_: SessionMessageCompactionCompletedType
    cost: float | Unset = UNSET
    metadata: SessionMessageCompactionCompletedMetadata | Unset = UNSET
    model: ModelRef | Unset = UNSET
    provider_context: SessionProviderContext | Unset = UNSET
    provider_state: SessionMessageProviderState5 | Unset = UNSET
    tokens: TokenUsageInfo | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.session_message_compaction_completed_metadata import SessionMessageCompactionCompletedMetadata # noqa: PLC0415
        from ..models.session_message_compaction_completed_time import SessionMessageCompactionCompletedTime # noqa: PLC0415
        from ..models.session_message_provider_state_5 import SessionMessageProviderState5 # noqa: PLC0415
        from ..models.session_provider_context import SessionProviderContext # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        id = self.id

        reason = self.reason.value

        recent = self.recent

        status = self.status.value

        summary = self.summary

        time = self.time.to_dict()

        type_ = self.type_.value

        cost = self.cost

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        provider_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_context, Unset):
            provider_context = self.provider_context.to_dict()

        provider_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_state, Unset):
            provider_state = self.provider_state.to_dict()

        tokens: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = self.tokens.to_dict()


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
        if cost is not UNSET:
            field_dict["cost"] = cost
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if model is not UNSET:
            field_dict["model"] = model
        if provider_context is not UNSET:
            field_dict["providerContext"] = provider_context
        if provider_state is not UNSET:
            field_dict["providerState"] = provider_state
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.session_message_compaction_completed_metadata import SessionMessageCompactionCompletedMetadata # noqa: PLC0415
        from ..models.session_message_compaction_completed_time import SessionMessageCompactionCompletedTime # noqa: PLC0415
        from ..models.session_message_provider_state_5 import SessionMessageProviderState5 # noqa: PLC0415
        from ..models.session_provider_context import SessionProviderContext # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        reason = SessionMessageCompactionCompletedReason(d.pop("reason"))




        recent = d.pop("recent")

        status = SessionMessageCompactionCompletedStatus(d.pop("status"))




        summary = d.pop("summary")

        time = SessionMessageCompactionCompletedTime.from_dict(d.pop("time"))




        type_ = SessionMessageCompactionCompletedType(d.pop("type"))




        cost = d.pop("cost", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageCompactionCompletedMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageCompactionCompletedMetadata.from_dict(_metadata)




        _model = d.pop("model", UNSET)
        model: ModelRef | Unset
        if isinstance(_model,  Unset):
            model = UNSET
        else:
            model = ModelRef.from_dict(_model)




        _provider_context = d.pop("providerContext", UNSET)
        provider_context: SessionProviderContext | Unset
        if isinstance(_provider_context,  Unset):
            provider_context = UNSET
        else:
            provider_context = SessionProviderContext.from_dict(_provider_context)




        _provider_state = d.pop("providerState", UNSET)
        provider_state: SessionMessageProviderState5 | Unset
        if isinstance(_provider_state,  Unset):
            provider_state = UNSET
        else:
            provider_state = SessionMessageProviderState5.from_dict(_provider_state)




        _tokens = d.pop("tokens", UNSET)
        tokens: TokenUsageInfo | Unset
        if isinstance(_tokens,  Unset):
            tokens = UNSET
        else:
            tokens = TokenUsageInfo.from_dict(_tokens)




        session_message_compaction_completed = cls(
            id=id,
            reason=reason,
            recent=recent,
            status=status,
            summary=summary,
            time=time,
            type_=type_,
            cost=cost,
            metadata=metadata,
            model=model,
            provider_context=provider_context,
            provider_state=provider_state,
            tokens=tokens,
        )

        return session_message_compaction_completed

