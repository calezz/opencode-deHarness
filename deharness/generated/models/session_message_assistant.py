from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_assistant_finish import SessionMessageAssistantFinish
from ..models.session_message_assistant_type import SessionMessageAssistantType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.model_ref import ModelRef
  from ..models.session_message_assistant_metadata import SessionMessageAssistantMetadata
  from ..models.session_message_assistant_reasoning import SessionMessageAssistantReasoning
  from ..models.session_message_assistant_retry import SessionMessageAssistantRetry
  from ..models.session_message_assistant_snapshot import SessionMessageAssistantSnapshot
  from ..models.session_message_assistant_text import SessionMessageAssistantText
  from ..models.session_message_assistant_time import SessionMessageAssistantTime
  from ..models.session_message_assistant_tool import SessionMessageAssistantTool
  from ..models.session_message_provider_state_4 import SessionMessageProviderState4
  from ..models.session_structured_error import SessionStructuredError
  from ..models.token_usage_info import TokenUsageInfo





T = TypeVar("T", bound="SessionMessageAssistant")



@_attrs_define
class SessionMessageAssistant:
    """ 
        Attributes:
            agent (str):
            content (list[SessionMessageAssistantReasoning | SessionMessageAssistantText | SessionMessageAssistantTool]):
            id (str):
            model (ModelRef):
            time (SessionMessageAssistantTime):
            type_ (SessionMessageAssistantType):
            cost (float | Unset):
            error (SessionStructuredError | Unset):
            finish (SessionMessageAssistantFinish | Unset):
            metadata (SessionMessageAssistantMetadata | Unset):
            provider_state (SessionMessageProviderState4 | Unset):
            raw_finish (str | Unset):
            retry (SessionMessageAssistantRetry | Unset):
            snapshot (SessionMessageAssistantSnapshot | Unset):
            tokens (TokenUsageInfo | Unset):
     """

    agent: str
    content: list[SessionMessageAssistantReasoning | SessionMessageAssistantText | SessionMessageAssistantTool]
    id: str
    model: ModelRef
    time: SessionMessageAssistantTime
    type_: SessionMessageAssistantType
    cost: float | Unset = UNSET
    error: SessionStructuredError | Unset = UNSET
    finish: SessionMessageAssistantFinish | Unset = UNSET
    metadata: SessionMessageAssistantMetadata | Unset = UNSET
    provider_state: SessionMessageProviderState4 | Unset = UNSET
    raw_finish: str | Unset = UNSET
    retry: SessionMessageAssistantRetry | Unset = UNSET
    snapshot: SessionMessageAssistantSnapshot | Unset = UNSET
    tokens: TokenUsageInfo | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.session_message_assistant_metadata import SessionMessageAssistantMetadata # noqa: PLC0415
        from ..models.session_message_assistant_reasoning import SessionMessageAssistantReasoning # noqa: PLC0415
        from ..models.session_message_assistant_retry import SessionMessageAssistantRetry # noqa: PLC0415
        from ..models.session_message_assistant_snapshot import SessionMessageAssistantSnapshot # noqa: PLC0415
        from ..models.session_message_assistant_text import SessionMessageAssistantText # noqa: PLC0415
        from ..models.session_message_assistant_time import SessionMessageAssistantTime # noqa: PLC0415
        from ..models.session_message_assistant_tool import SessionMessageAssistantTool # noqa: PLC0415
        from ..models.session_message_provider_state_4 import SessionMessageProviderState4 # noqa: PLC0415
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        agent = self.agent

        content = []
        for content_item_data in self.content:
            content_item: dict[str, Any]
            if isinstance(content_item_data, SessionMessageAssistantText):
                content_item = content_item_data.to_dict()
            elif isinstance(content_item_data, SessionMessageAssistantReasoning):
                content_item = content_item_data.to_dict()
            else:
                content_item = content_item_data.to_dict()

            content.append(content_item)



        id = self.id

        model = self.model.to_dict()

        time = self.time.to_dict()

        type_ = self.type_.value

        cost = self.cost

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        finish: str | Unset = UNSET
        if not isinstance(self.finish, Unset):
            finish = self.finish.value


        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        provider_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_state, Unset):
            provider_state = self.provider_state.to_dict()

        raw_finish = self.raw_finish

        retry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry, Unset):
            retry = self.retry.to_dict()

        snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snapshot, Unset):
            snapshot = self.snapshot.to_dict()

        tokens: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tokens, Unset):
            tokens = self.tokens.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
            "content": content,
            "id": id,
            "model": model,
            "time": time,
            "type": type_,
        })
        if cost is not UNSET:
            field_dict["cost"] = cost
        if error is not UNSET:
            field_dict["error"] = error
        if finish is not UNSET:
            field_dict["finish"] = finish
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if provider_state is not UNSET:
            field_dict["providerState"] = provider_state
        if raw_finish is not UNSET:
            field_dict["rawFinish"] = raw_finish
        if retry is not UNSET:
            field_dict["retry"] = retry
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.session_message_assistant_metadata import SessionMessageAssistantMetadata # noqa: PLC0415
        from ..models.session_message_assistant_reasoning import SessionMessageAssistantReasoning # noqa: PLC0415
        from ..models.session_message_assistant_retry import SessionMessageAssistantRetry # noqa: PLC0415
        from ..models.session_message_assistant_snapshot import SessionMessageAssistantSnapshot # noqa: PLC0415
        from ..models.session_message_assistant_text import SessionMessageAssistantText # noqa: PLC0415
        from ..models.session_message_assistant_time import SessionMessageAssistantTime # noqa: PLC0415
        from ..models.session_message_assistant_tool import SessionMessageAssistantTool # noqa: PLC0415
        from ..models.session_message_provider_state_4 import SessionMessageProviderState4 # noqa: PLC0415
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        from ..models.token_usage_info import TokenUsageInfo # noqa: PLC0415
        d = dict(src_dict)
        agent = d.pop("agent")

        content = []
        _content = d.pop("content")
        for content_item_data in (_content):
            def _parse_content_item(data: object) -> SessionMessageAssistantReasoning | SessionMessageAssistantText | SessionMessageAssistantTool:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    content_item_type_0 = SessionMessageAssistantText.from_dict(data)



                    return content_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    content_item_type_1 = SessionMessageAssistantReasoning.from_dict(data)



                    return content_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                content_item_type_2 = SessionMessageAssistantTool.from_dict(data)



                return content_item_type_2

            content_item = _parse_content_item(content_item_data)

            content.append(content_item)


        id = d.pop("id")

        model = ModelRef.from_dict(d.pop("model"))




        time = SessionMessageAssistantTime.from_dict(d.pop("time"))




        type_ = SessionMessageAssistantType(d.pop("type"))




        cost = d.pop("cost", UNSET)

        _error = d.pop("error", UNSET)
        error: SessionStructuredError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = SessionStructuredError.from_dict(_error)




        _finish = d.pop("finish", UNSET)
        finish: SessionMessageAssistantFinish | Unset
        if isinstance(_finish,  Unset):
            finish = UNSET
        else:
            finish = SessionMessageAssistantFinish(_finish)




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageAssistantMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageAssistantMetadata.from_dict(_metadata)




        _provider_state = d.pop("providerState", UNSET)
        provider_state: SessionMessageProviderState4 | Unset
        if isinstance(_provider_state,  Unset):
            provider_state = UNSET
        else:
            provider_state = SessionMessageProviderState4.from_dict(_provider_state)




        raw_finish = d.pop("rawFinish", UNSET)

        _retry = d.pop("retry", UNSET)
        retry: SessionMessageAssistantRetry | Unset
        if isinstance(_retry,  Unset):
            retry = UNSET
        else:
            retry = SessionMessageAssistantRetry.from_dict(_retry)




        _snapshot = d.pop("snapshot", UNSET)
        snapshot: SessionMessageAssistantSnapshot | Unset
        if isinstance(_snapshot,  Unset):
            snapshot = UNSET
        else:
            snapshot = SessionMessageAssistantSnapshot.from_dict(_snapshot)




        _tokens = d.pop("tokens", UNSET)
        tokens: TokenUsageInfo | Unset
        if isinstance(_tokens,  Unset):
            tokens = UNSET
        else:
            tokens = TokenUsageInfo.from_dict(_tokens)




        session_message_assistant = cls(
            agent=agent,
            content=content,
            id=id,
            model=model,
            time=time,
            type_=type_,
            cost=cost,
            error=error,
            finish=finish,
            metadata=metadata,
            provider_state=provider_state,
            raw_finish=raw_finish,
            retry=retry,
            snapshot=snapshot,
            tokens=tokens,
        )

        return session_message_assistant

