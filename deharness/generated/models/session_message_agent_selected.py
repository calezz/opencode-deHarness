from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_agent_selected_type import SessionMessageAgentSelectedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_agent_selected_metadata import SessionMessageAgentSelectedMetadata
  from ..models.session_message_agent_selected_time import SessionMessageAgentSelectedTime





T = TypeVar("T", bound="SessionMessageAgentSelected")



@_attrs_define
class SessionMessageAgentSelected:
    """ 
        Attributes:
            agent (str):
            id (str):
            time (SessionMessageAgentSelectedTime):
            type_ (SessionMessageAgentSelectedType):
            metadata (SessionMessageAgentSelectedMetadata | Unset):
            previous (str | Unset):
     """

    agent: str
    id: str
    time: SessionMessageAgentSelectedTime
    type_: SessionMessageAgentSelectedType
    metadata: SessionMessageAgentSelectedMetadata | Unset = UNSET
    previous: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_agent_selected_metadata import SessionMessageAgentSelectedMetadata # noqa: PLC0415
        from ..models.session_message_agent_selected_time import SessionMessageAgentSelectedTime # noqa: PLC0415
        agent = self.agent

        id = self.id

        time = self.time.to_dict()

        type_ = self.type_.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        previous = self.previous


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
            "id": id,
            "time": time,
            "type": type_,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_agent_selected_metadata import SessionMessageAgentSelectedMetadata # noqa: PLC0415
        from ..models.session_message_agent_selected_time import SessionMessageAgentSelectedTime # noqa: PLC0415
        d = dict(src_dict)
        agent = d.pop("agent")

        id = d.pop("id")

        time = SessionMessageAgentSelectedTime.from_dict(d.pop("time"))




        type_ = SessionMessageAgentSelectedType(d.pop("type"))




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageAgentSelectedMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageAgentSelectedMetadata.from_dict(_metadata)




        previous = d.pop("previous", UNSET)

        session_message_agent_selected = cls(
            agent=agent,
            id=id,
            time=time,
            type_=type_,
            metadata=metadata,
            previous=previous,
        )

        return session_message_agent_selected

