from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_system_type import SessionMessageSystemType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_system_metadata import SessionMessageSystemMetadata
  from ..models.session_message_system_time import SessionMessageSystemTime





T = TypeVar("T", bound="SessionMessageSystem")



@_attrs_define
class SessionMessageSystem:
    """ 
        Attributes:
            id (str):
            text (str):
            time (SessionMessageSystemTime):
            type_ (SessionMessageSystemType):
            description (str | Unset):
            metadata (SessionMessageSystemMetadata | Unset):
     """

    id: str
    text: str
    time: SessionMessageSystemTime
    type_: SessionMessageSystemType
    description: str | Unset = UNSET
    metadata: SessionMessageSystemMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_system_metadata import SessionMessageSystemMetadata # noqa: PLC0415
        from ..models.session_message_system_time import SessionMessageSystemTime # noqa: PLC0415
        id = self.id

        text = self.text

        time = self.time.to_dict()

        type_ = self.type_.value

        description = self.description

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "text": text,
            "time": time,
            "type": type_,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_message_system_metadata import SessionMessageSystemMetadata # noqa: PLC0415
        from ..models.session_message_system_time import SessionMessageSystemTime # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        time = SessionMessageSystemTime.from_dict(d.pop("time"))




        type_ = SessionMessageSystemType(d.pop("type"))




        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageSystemMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageSystemMetadata.from_dict(_metadata)




        session_message_system = cls(
            id=id,
            text=text,
            time=time,
            type_=type_,
            description=description,
            metadata=metadata,
        )

        return session_message_system

