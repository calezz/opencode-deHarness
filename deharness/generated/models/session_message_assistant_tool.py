from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_assistant_tool_type import SessionMessageAssistantToolType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_assistant_tool_time import SessionMessageAssistantToolTime
  from ..models.session_message_provider_state_2 import SessionMessageProviderState2
  from ..models.session_message_provider_state_3 import SessionMessageProviderState3
  from ..models.session_message_tool_state_completed import SessionMessageToolStateCompleted
  from ..models.session_message_tool_state_error import SessionMessageToolStateError
  from ..models.session_message_tool_state_running import SessionMessageToolStateRunning
  from ..models.session_message_tool_state_streaming import SessionMessageToolStateStreaming





T = TypeVar("T", bound="SessionMessageAssistantTool")



@_attrs_define
class SessionMessageAssistantTool:
    """ 
        Attributes:
            id (str):
            name (str):
            state (SessionMessageToolStateCompleted | SessionMessageToolStateError | SessionMessageToolStateRunning |
                SessionMessageToolStateStreaming):
            time (SessionMessageAssistantToolTime):
            type_ (SessionMessageAssistantToolType):
            executed (bool | Unset):
            provider_result_state (SessionMessageProviderState3 | Unset):
            provider_state (SessionMessageProviderState2 | Unset):
     """

    id: str
    name: str
    state: SessionMessageToolStateCompleted | SessionMessageToolStateError | SessionMessageToolStateRunning | SessionMessageToolStateStreaming
    time: SessionMessageAssistantToolTime
    type_: SessionMessageAssistantToolType
    executed: bool | Unset = UNSET
    provider_result_state: SessionMessageProviderState3 | Unset = UNSET
    provider_state: SessionMessageProviderState2 | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_assistant_tool_time import SessionMessageAssistantToolTime # noqa: PLC0415
        from ..models.session_message_provider_state_2 import SessionMessageProviderState2 # noqa: PLC0415
        from ..models.session_message_provider_state_3 import SessionMessageProviderState3 # noqa: PLC0415
        from ..models.session_message_tool_state_completed import SessionMessageToolStateCompleted # noqa: PLC0415
        from ..models.session_message_tool_state_error import SessionMessageToolStateError # noqa: PLC0415
        from ..models.session_message_tool_state_running import SessionMessageToolStateRunning # noqa: PLC0415
        from ..models.session_message_tool_state_streaming import SessionMessageToolStateStreaming # noqa: PLC0415
        id = self.id

        name = self.name

        state: dict[str, Any]
        if isinstance(self.state, SessionMessageToolStateStreaming):
            state = self.state.to_dict()
        elif isinstance(self.state, SessionMessageToolStateRunning):
            state = self.state.to_dict()
        elif isinstance(self.state, SessionMessageToolStateCompleted):
            state = self.state.to_dict()
        else:
            state = self.state.to_dict()


        time = self.time.to_dict()

        type_ = self.type_.value

        executed = self.executed

        provider_result_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_result_state, Unset):
            provider_result_state = self.provider_result_state.to_dict()

        provider_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider_state, Unset):
            provider_state = self.provider_state.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "state": state,
            "time": time,
            "type": type_,
        })
        if executed is not UNSET:
            field_dict["executed"] = executed
        if provider_result_state is not UNSET:
            field_dict["providerResultState"] = provider_result_state
        if provider_state is not UNSET:
            field_dict["providerState"] = provider_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_assistant_tool_time import SessionMessageAssistantToolTime # noqa: PLC0415
        from ..models.session_message_provider_state_2 import SessionMessageProviderState2 # noqa: PLC0415
        from ..models.session_message_provider_state_3 import SessionMessageProviderState3 # noqa: PLC0415
        from ..models.session_message_tool_state_completed import SessionMessageToolStateCompleted # noqa: PLC0415
        from ..models.session_message_tool_state_error import SessionMessageToolStateError # noqa: PLC0415
        from ..models.session_message_tool_state_running import SessionMessageToolStateRunning # noqa: PLC0415
        from ..models.session_message_tool_state_streaming import SessionMessageToolStateStreaming # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_state(data: object) -> SessionMessageToolStateCompleted | SessionMessageToolStateError | SessionMessageToolStateRunning | SessionMessageToolStateStreaming:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_0 = SessionMessageToolStateStreaming.from_dict(data)



                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_1 = SessionMessageToolStateRunning.from_dict(data)



                return state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_type_2 = SessionMessageToolStateCompleted.from_dict(data)



                return state_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            state_type_3 = SessionMessageToolStateError.from_dict(data)



            return state_type_3

        state = _parse_state(d.pop("state"))


        time = SessionMessageAssistantToolTime.from_dict(d.pop("time"))




        type_ = SessionMessageAssistantToolType(d.pop("type"))




        executed = d.pop("executed", UNSET)

        _provider_result_state = d.pop("providerResultState", UNSET)
        provider_result_state: SessionMessageProviderState3 | Unset
        if isinstance(_provider_result_state,  Unset):
            provider_result_state = UNSET
        else:
            provider_result_state = SessionMessageProviderState3.from_dict(_provider_result_state)




        _provider_state = d.pop("providerState", UNSET)
        provider_state: SessionMessageProviderState2 | Unset
        if isinstance(_provider_state,  Unset):
            provider_state = UNSET
        else:
            provider_state = SessionMessageProviderState2.from_dict(_provider_state)




        session_message_assistant_tool = cls(
            id=id,
            name=name,
            state=state,
            time=time,
            type_=type_,
            executed=executed,
            provider_result_state=provider_result_state,
            provider_state=provider_state,
        )

        return session_message_assistant_tool

