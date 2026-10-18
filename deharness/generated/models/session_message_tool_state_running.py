from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_tool_state_running_status import SessionMessageToolStateRunningStatus
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_tool_state_running_input import SessionMessageToolStateRunningInput
  from ..models.session_message_tool_state_running_metadata import SessionMessageToolStateRunningMetadata





T = TypeVar("T", bound="SessionMessageToolStateRunning")



@_attrs_define
class SessionMessageToolStateRunning:
    """ 
        Attributes:
            input_ (SessionMessageToolStateRunningInput):
            metadata (SessionMessageToolStateRunningMetadata):
            status (SessionMessageToolStateRunningStatus):
     """

    input_: SessionMessageToolStateRunningInput
    metadata: SessionMessageToolStateRunningMetadata
    status: SessionMessageToolStateRunningStatus





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_tool_state_running_input import SessionMessageToolStateRunningInput # noqa: PLC0415
        from ..models.session_message_tool_state_running_metadata import SessionMessageToolStateRunningMetadata # noqa: PLC0415
        input_ = self.input_.to_dict()

        metadata = self.metadata.to_dict()

        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "input": input_,
            "metadata": metadata,
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_tool_state_running_input import SessionMessageToolStateRunningInput # noqa: PLC0415
        from ..models.session_message_tool_state_running_metadata import SessionMessageToolStateRunningMetadata # noqa: PLC0415
        d = dict(src_dict)
        input_ = SessionMessageToolStateRunningInput.from_dict(d.pop("input"))




        metadata = SessionMessageToolStateRunningMetadata.from_dict(d.pop("metadata"))




        status = SessionMessageToolStateRunningStatus(d.pop("status"))




        session_message_tool_state_running = cls(
            input_=input_,
            metadata=metadata,
            status=status,
        )

        return session_message_tool_state_running

