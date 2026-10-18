from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.session_info import SessionInfo
  from ..models.session_message_agent_selected import SessionMessageAgentSelected
  from ..models.session_message_assistant import SessionMessageAssistant
  from ..models.session_message_compaction_completed import SessionMessageCompactionCompleted
  from ..models.session_message_compaction_failed import SessionMessageCompactionFailed
  from ..models.session_message_compaction_running import SessionMessageCompactionRunning
  from ..models.session_message_idle import SessionMessageIdle
  from ..models.session_message_location_switched import SessionMessageLocationSwitched
  from ..models.session_message_model_selected import SessionMessageModelSelected
  from ..models.session_message_shell import SessionMessageShell
  from ..models.session_message_skill import SessionMessageSkill
  from ..models.session_message_synthetic import SessionMessageSynthetic
  from ..models.session_message_system import SessionMessageSystem
  from ..models.session_message_user import SessionMessageUser





T = TypeVar("T", bound="SessionTransferData")



@_attrs_define
class SessionTransferData:
    """ 
        Attributes:
            info (SessionInfo):
            messages (list[SessionMessageAgentSelected | SessionMessageAssistant | SessionMessageCompactionCompleted |
                SessionMessageCompactionFailed | SessionMessageCompactionRunning | SessionMessageIdle |
                SessionMessageLocationSwitched | SessionMessageModelSelected | SessionMessageShell | SessionMessageSkill |
                SessionMessageSynthetic | SessionMessageSystem | SessionMessageUser]):
     """

    info: SessionInfo
    messages: list[SessionMessageAgentSelected | SessionMessageAssistant | SessionMessageCompactionCompleted | SessionMessageCompactionFailed | SessionMessageCompactionRunning | SessionMessageIdle | SessionMessageLocationSwitched | SessionMessageModelSelected | SessionMessageShell | SessionMessageSkill | SessionMessageSynthetic | SessionMessageSystem | SessionMessageUser]





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_info import SessionInfo # noqa: PLC0415
        from ..models.session_message_agent_selected import SessionMessageAgentSelected # noqa: PLC0415
        from ..models.session_message_assistant import SessionMessageAssistant # noqa: PLC0415
        from ..models.session_message_compaction_completed import SessionMessageCompactionCompleted # noqa: PLC0415
        from ..models.session_message_compaction_failed import SessionMessageCompactionFailed # noqa: PLC0415
        from ..models.session_message_compaction_running import SessionMessageCompactionRunning # noqa: PLC0415
        from ..models.session_message_idle import SessionMessageIdle # noqa: PLC0415
        from ..models.session_message_location_switched import SessionMessageLocationSwitched # noqa: PLC0415
        from ..models.session_message_model_selected import SessionMessageModelSelected # noqa: PLC0415
        from ..models.session_message_shell import SessionMessageShell # noqa: PLC0415
        from ..models.session_message_skill import SessionMessageSkill # noqa: PLC0415
        from ..models.session_message_synthetic import SessionMessageSynthetic # noqa: PLC0415
        from ..models.session_message_system import SessionMessageSystem # noqa: PLC0415
        from ..models.session_message_user import SessionMessageUser # noqa: PLC0415
        info = self.info.to_dict()

        messages = []
        for messages_item_data in self.messages:
            messages_item: dict[str, Any]
            if isinstance(messages_item_data, SessionMessageAgentSelected):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageModelSelected):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageLocationSwitched):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageUser):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageSynthetic):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageSystem):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageSkill):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageShell):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageAssistant):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageCompactionRunning):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageCompactionCompleted):
                messages_item = messages_item_data.to_dict()
            elif isinstance(messages_item_data, SessionMessageCompactionFailed):
                messages_item = messages_item_data.to_dict()
            else:
                messages_item = messages_item_data.to_dict()

            messages.append(messages_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "info": info,
            "messages": messages,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_info import SessionInfo # noqa: PLC0415
        from ..models.session_message_agent_selected import SessionMessageAgentSelected # noqa: PLC0415
        from ..models.session_message_assistant import SessionMessageAssistant # noqa: PLC0415
        from ..models.session_message_compaction_completed import SessionMessageCompactionCompleted # noqa: PLC0415
        from ..models.session_message_compaction_failed import SessionMessageCompactionFailed # noqa: PLC0415
        from ..models.session_message_compaction_running import SessionMessageCompactionRunning # noqa: PLC0415
        from ..models.session_message_idle import SessionMessageIdle # noqa: PLC0415
        from ..models.session_message_location_switched import SessionMessageLocationSwitched # noqa: PLC0415
        from ..models.session_message_model_selected import SessionMessageModelSelected # noqa: PLC0415
        from ..models.session_message_shell import SessionMessageShell # noqa: PLC0415
        from ..models.session_message_skill import SessionMessageSkill # noqa: PLC0415
        from ..models.session_message_synthetic import SessionMessageSynthetic # noqa: PLC0415
        from ..models.session_message_system import SessionMessageSystem # noqa: PLC0415
        from ..models.session_message_user import SessionMessageUser # noqa: PLC0415
        d = dict(src_dict)
        info = SessionInfo.from_dict(d.pop("info"))




        messages = []
        _messages = d.pop("messages")
        for messages_item_data in (_messages):
            def _parse_messages_item(data: object) -> SessionMessageAgentSelected | SessionMessageAssistant | SessionMessageCompactionCompleted | SessionMessageCompactionFailed | SessionMessageCompactionRunning | SessionMessageIdle | SessionMessageLocationSwitched | SessionMessageModelSelected | SessionMessageShell | SessionMessageSkill | SessionMessageSynthetic | SessionMessageSystem | SessionMessageUser:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_0 = SessionMessageAgentSelected.from_dict(data)



                    return componentsschemas_session_message_info_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_1 = SessionMessageModelSelected.from_dict(data)



                    return componentsschemas_session_message_info_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_2 = SessionMessageLocationSwitched.from_dict(data)



                    return componentsschemas_session_message_info_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_3 = SessionMessageUser.from_dict(data)



                    return componentsschemas_session_message_info_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_4 = SessionMessageSynthetic.from_dict(data)



                    return componentsschemas_session_message_info_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_5 = SessionMessageSystem.from_dict(data)



                    return componentsschemas_session_message_info_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_6 = SessionMessageSkill.from_dict(data)



                    return componentsschemas_session_message_info_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_7 = SessionMessageShell.from_dict(data)



                    return componentsschemas_session_message_info_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_info_type_8 = SessionMessageAssistant.from_dict(data)



                    return componentsschemas_session_message_info_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_compaction_type_0 = SessionMessageCompactionRunning.from_dict(data)



                    return componentsschemas_session_message_compaction_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_compaction_type_1 = SessionMessageCompactionCompleted.from_dict(data)



                    return componentsschemas_session_message_compaction_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_session_message_compaction_type_2 = SessionMessageCompactionFailed.from_dict(data)



                    return componentsschemas_session_message_compaction_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_session_message_info_type_10 = SessionMessageIdle.from_dict(data)



                return componentsschemas_session_message_info_type_10

            messages_item = _parse_messages_item(messages_item_data)

            messages.append(messages_item)


        session_transfer_data = cls(
            info=info,
            messages=messages,
        )

        return session_transfer_data

