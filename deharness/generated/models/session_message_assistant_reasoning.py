from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_assistant_reasoning_type import SessionMessageAssistantReasoningType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_assistant_reasoning_time import SessionMessageAssistantReasoningTime
  from ..models.session_message_provider_state_1 import SessionMessageProviderState1





T = TypeVar("T", bound="SessionMessageAssistantReasoning")



@_attrs_define
class SessionMessageAssistantReasoning:
    """ 
        Attributes:
            text (str):
            type_ (SessionMessageAssistantReasoningType):
            state (SessionMessageProviderState1 | Unset):
            time (SessionMessageAssistantReasoningTime | Unset):
     """

    text: str
    type_: SessionMessageAssistantReasoningType
    state: SessionMessageProviderState1 | Unset = UNSET
    time: SessionMessageAssistantReasoningTime | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_assistant_reasoning_time import SessionMessageAssistantReasoningTime # noqa: PLC0415
        from ..models.session_message_provider_state_1 import SessionMessageProviderState1 # noqa: PLC0415
        text = self.text

        type_ = self.type_.value

        state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
            "type": type_,
        })
        if state is not UNSET:
            field_dict["state"] = state
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_assistant_reasoning_time import SessionMessageAssistantReasoningTime # noqa: PLC0415
        from ..models.session_message_provider_state_1 import SessionMessageProviderState1 # noqa: PLC0415
        d = dict(src_dict)
        text = d.pop("text")

        type_ = SessionMessageAssistantReasoningType(d.pop("type"))




        _state = d.pop("state", UNSET)
        state: SessionMessageProviderState1 | Unset
        if isinstance(_state,  Unset):
            state = UNSET
        else:
            state = SessionMessageProviderState1.from_dict(_state)




        _time = d.pop("time", UNSET)
        time: SessionMessageAssistantReasoningTime | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = SessionMessageAssistantReasoningTime.from_dict(_time)




        session_message_assistant_reasoning = cls(
            text=text,
            type_=type_,
            state=state,
            time=time,
        )

        return session_message_assistant_reasoning

