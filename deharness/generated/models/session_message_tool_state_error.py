from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_tool_state_error_status import SessionMessageToolStateErrorStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_tool_state_error_input import SessionMessageToolStateErrorInput
  from ..models.session_message_tool_state_error_metadata import SessionMessageToolStateErrorMetadata
  from ..models.session_structured_error import SessionStructuredError
  from ..models.tool_file_content import ToolFileContent
  from ..models.tool_text_content import ToolTextContent





T = TypeVar("T", bound="SessionMessageToolStateError")



@_attrs_define
class SessionMessageToolStateError:
    """ 
        Attributes:
            error (SessionStructuredError):
            input_ (SessionMessageToolStateErrorInput):
            status (SessionMessageToolStateErrorStatus):
            content (list[ToolFileContent | ToolTextContent] | Unset):
            metadata (SessionMessageToolStateErrorMetadata | Unset):
     """

    error: SessionStructuredError
    input_: SessionMessageToolStateErrorInput
    status: SessionMessageToolStateErrorStatus
    content: list[ToolFileContent | ToolTextContent] | Unset = UNSET
    metadata: SessionMessageToolStateErrorMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_tool_state_error_input import SessionMessageToolStateErrorInput # noqa: PLC0415
        from ..models.session_message_tool_state_error_metadata import SessionMessageToolStateErrorMetadata # noqa: PLC0415
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        from ..models.tool_file_content import ToolFileContent # noqa: PLC0415
        from ..models.tool_text_content import ToolTextContent # noqa: PLC0415
        error = self.error.to_dict()

        input_ = self.input_.to_dict()

        status = self.status.value

        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item: dict[str, Any]
                if isinstance(content_item_data, ToolTextContent):
                    content_item = content_item_data.to_dict()
                else:
                    content_item = content_item_data.to_dict()

                content.append(content_item)



        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "input": input_,
            "status": status,
        })
        if content is not UNSET:
            field_dict["content"] = content
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_tool_state_error_input import SessionMessageToolStateErrorInput # noqa: PLC0415
        from ..models.session_message_tool_state_error_metadata import SessionMessageToolStateErrorMetadata # noqa: PLC0415
        from ..models.session_structured_error import SessionStructuredError # noqa: PLC0415
        from ..models.tool_file_content import ToolFileContent # noqa: PLC0415
        from ..models.tool_text_content import ToolTextContent # noqa: PLC0415
        d = dict(src_dict)
        error = SessionStructuredError.from_dict(d.pop("error"))




        input_ = SessionMessageToolStateErrorInput.from_dict(d.pop("input"))




        status = SessionMessageToolStateErrorStatus(d.pop("status"))




        _content = d.pop("content", UNSET)
        content: list[ToolFileContent | ToolTextContent] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
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


        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageToolStateErrorMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageToolStateErrorMetadata.from_dict(_metadata)




        session_message_tool_state_error = cls(
            error=error,
            input_=input_,
            status=status,
            content=content,
            metadata=metadata,
        )

        return session_message_tool_state_error

