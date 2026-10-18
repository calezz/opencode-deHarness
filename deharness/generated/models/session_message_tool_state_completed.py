from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_tool_state_completed_status import SessionMessageToolStateCompletedStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_tool_state_completed_input import SessionMessageToolStateCompletedInput
  from ..models.session_message_tool_state_completed_metadata import SessionMessageToolStateCompletedMetadata
  from ..models.tool_file_content import ToolFileContent
  from ..models.tool_text_content import ToolTextContent





T = TypeVar("T", bound="SessionMessageToolStateCompleted")



@_attrs_define
class SessionMessageToolStateCompleted:
    """ 
        Attributes:
            content (list[ToolFileContent | ToolTextContent]):
            input_ (SessionMessageToolStateCompletedInput):
            status (SessionMessageToolStateCompletedStatus):
            metadata (SessionMessageToolStateCompletedMetadata | Unset):
     """

    content: list[ToolFileContent | ToolTextContent]
    input_: SessionMessageToolStateCompletedInput
    status: SessionMessageToolStateCompletedStatus
    metadata: SessionMessageToolStateCompletedMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_tool_state_completed_input import SessionMessageToolStateCompletedInput # noqa: PLC0415
        from ..models.session_message_tool_state_completed_metadata import SessionMessageToolStateCompletedMetadata # noqa: PLC0415
        from ..models.tool_file_content import ToolFileContent # noqa: PLC0415
        from ..models.tool_text_content import ToolTextContent # noqa: PLC0415
        content = []
        for content_item_data in self.content:
            content_item: dict[str, Any]
            if isinstance(content_item_data, ToolTextContent):
                content_item = content_item_data.to_dict()
            else:
                content_item = content_item_data.to_dict()

            content.append(content_item)



        input_ = self.input_.to_dict()

        status = self.status.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "content": content,
            "input": input_,
            "status": status,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_tool_state_completed_input import SessionMessageToolStateCompletedInput # noqa: PLC0415
        from ..models.session_message_tool_state_completed_metadata import SessionMessageToolStateCompletedMetadata # noqa: PLC0415
        from ..models.tool_file_content import ToolFileContent # noqa: PLC0415
        from ..models.tool_text_content import ToolTextContent # noqa: PLC0415
        d = dict(src_dict)
        content = []
        _content = d.pop("content")
        for content_item_data in (_content):
            def _parse_content_item(data: object) -> ToolFileContent | ToolTextContent:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_tool_content_type_0 = ToolTextContent.from_dict(data)



                    return componentsschemas_tool_content_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_tool_content_type_1 = ToolFileContent.from_dict(data)



                return componentsschemas_tool_content_type_1

            content_item = _parse_content_item(content_item_data)

            content.append(content_item)


        input_ = SessionMessageToolStateCompletedInput.from_dict(d.pop("input"))




        status = SessionMessageToolStateCompletedStatus(d.pop("status"))




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageToolStateCompletedMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageToolStateCompletedMetadata.from_dict(_metadata)




        session_message_tool_state_completed = cls(
            content=content,
            input_=input_,
            status=status,
            metadata=metadata,
        )

        return session_message_tool_state_completed

