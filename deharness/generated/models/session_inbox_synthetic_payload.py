from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_inbox_synthetic_payload_metadata import SessionInboxSyntheticPayloadMetadata





T = TypeVar("T", bound="SessionInboxSyntheticPayload")



@_attrs_define
class SessionInboxSyntheticPayload:
    """ 
        Attributes:
            text (str):
            description (str | Unset):
            metadata (SessionInboxSyntheticPayloadMetadata | Unset):
     """

    text: str
    description: str | Unset = UNSET
    metadata: SessionInboxSyntheticPayloadMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_inbox_synthetic_payload_metadata import SessionInboxSyntheticPayloadMetadata # noqa: PLC0415
        text = self.text

        description = self.description

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_inbox_synthetic_payload_metadata import SessionInboxSyntheticPayloadMetadata # noqa: PLC0415
        d = dict(src_dict)
        text = d.pop("text")

        description = d.pop("description", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: SessionInboxSyntheticPayloadMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionInboxSyntheticPayloadMetadata.from_dict(_metadata)




        session_inbox_synthetic_payload = cls(
            text=text,
            description=description,
            metadata=metadata,
        )

        return session_inbox_synthetic_payload

