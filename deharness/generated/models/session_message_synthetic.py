from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_synthetic_type import SessionMessageSyntheticType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_message_synthetic_metadata import SessionMessageSyntheticMetadata
  from ..models.session_message_synthetic_time import SessionMessageSyntheticTime





T = TypeVar("T", bound="SessionMessageSynthetic")



@_attrs_define
class SessionMessageSynthetic:
    """ 
        Attributes:
            id (str):
            text (str):
            time (SessionMessageSyntheticTime):
            type_ (SessionMessageSyntheticType):
            description (str | Unset):
            metadata (SessionMessageSyntheticMetadata | Unset):
     """

    id: str
    text: str
    time: SessionMessageSyntheticTime
    type_: SessionMessageSyntheticType
    description: str | Unset = UNSET
    metadata: SessionMessageSyntheticMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_message_synthetic_metadata import SessionMessageSyntheticMetadata # noqa: PLC0415
        from ..models.session_message_synthetic_time import SessionMessageSyntheticTime # noqa: PLC0415
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
        from ..models.session_message_synthetic_metadata import SessionMessageSyntheticMetadata # noqa: PLC0415
        from ..models.session_message_synthetic_time import SessionMessageSyntheticTime # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        time = SessionMessageSyntheticTime.from_dict(d.pop("time"))




        type_ = SessionMessageSyntheticType(d.pop("type"))




        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageSyntheticMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageSyntheticMetadata.from_dict(_metadata)




        session_message_synthetic = cls(
            id=id,
            text=text,
            time=time,
            type_=type_,
            description=description,
            metadata=metadata,
        )

        return session_message_synthetic

