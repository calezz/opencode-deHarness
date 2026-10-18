from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
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
  from ..models.session_messages_response_cursor import SessionMessagesResponseCursor





T = TypeVar("T", bound="SessionMessagesResponse")



@_attrs_define
class SessionMessagesResponse:
    """ 
        Attributes:
            cursor (SessionMessagesResponseCursor):
            data (list[SessionMessageAgentSelected | SessionMessageAssistant | SessionMessageCompactionCompleted |
                SessionMessageCompactionFailed | SessionMessageCompactionRunning | SessionMessageIdle |
                SessionMessageLocationSwitched | SessionMessageModelSelected | SessionMessageShell | SessionMessageSkill |
                SessionMessageSynthetic | SessionMessageSystem | SessionMessageUser]):
     """

    cursor: SessionMessagesResponseCursor
    data: list[SessionMessageAgentSelected | SessionMessageAssistant | SessionMessageCompactionCompleted | SessionMessageCompactionFailed | SessionMessageCompactionRunning | SessionMessageIdle | SessionMessageLocationSwitched | SessionMessageModelSelected | SessionMessageShell | SessionMessageSkill | SessionMessageSynthetic | SessionMessageSystem | SessionMessageUser]





    def to_dict(self) -> dict[str, Any]:
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
        from ..models.session_messages_response_cursor import SessionMessagesResponseCursor # noqa: PLC0415
        cursor = self.cursor.to_dict()

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(data_item_data, SessionMessageAgentSelected):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageModelSelected):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageLocationSwitched):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageUser):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageSynthetic):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageSystem):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageSkill):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageShell):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageAssistant):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageCompactionRunning):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageCompactionCompleted):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, SessionMessageCompactionFailed):
                data_item = data_item_data.to_dict()
            else:
                data_item = data_item_data.to_dict()

            data.append(data_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cursor": cursor,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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
        from ..models.session_messages_response_cursor import SessionMessagesResponseCursor # noqa: PLC0415
        d = dict(src_dict)
        cursor = SessionMessagesResponseCursor.from_dict(d.pop("cursor"))




        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            def _parse_data_item(data: object) -> SessionMessageAgentSelected | SessionMessageAssistant | SessionMessageCompactionCompleted | SessionMessageCompactionFailed | SessionMessageCompactionRunning | SessionMessageIdle | SessionMessageLocationSwitched | SessionMessageModelSelected | SessionMessageShell | SessionMessageSkill | SessionMessageSynthetic | SessionMessageSystem | SessionMessageUser:
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

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)


        session_messages_response = cls(
            cursor=cursor,
            data=data,
        )

        return session_messages_response

