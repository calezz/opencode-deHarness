from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_inbox_delivery import SessionInboxDelivery
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.session_synthetic_body_metadata import SessionSyntheticBodyMetadata





T = TypeVar("T", bound="SessionSyntheticBody")



@_attrs_define
class SessionSyntheticBody:
    """ 
        Attributes:
            text (str):
            delivery (None | SessionInboxDelivery | Unset):
            description (None | str | Unset):
            id (None | str | Unset):
            metadata (SessionSyntheticBodyMetadata | Unset):
            resume (bool | None | Unset):
     """

    text: str
    delivery: None | SessionInboxDelivery | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    metadata: SessionSyntheticBodyMetadata | Unset = UNSET
    resume: bool | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_synthetic_body_metadata import SessionSyntheticBodyMetadata # noqa: PLC0415
        text = self.text

        delivery: None | str | Unset
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        elif isinstance(self.delivery, SessionInboxDelivery):
            delivery = self.delivery.value
        else:
            delivery = self.delivery

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        resume: bool | None | Unset
        if isinstance(self.resume, Unset):
            resume = UNSET
        else:
            resume = self.resume


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
        })
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if resume is not UNSET:
            field_dict["resume"] = resume

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_synthetic_body_metadata import SessionSyntheticBodyMetadata # noqa: PLC0415
        d = dict(src_dict)
        text = d.pop("text")

        def _parse_delivery(data: object) -> None | SessionInboxDelivery | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_type_0 = SessionInboxDelivery(data)



                return delivery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionInboxDelivery | Unset, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        _metadata = d.pop("metadata", UNSET)
        metadata: SessionSyntheticBodyMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionSyntheticBodyMetadata.from_dict(_metadata)




        def _parse_resume(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        resume = _parse_resume(d.pop("resume", UNSET))


        session_synthetic_body = cls(
            text=text,
            delivery=delivery,
            description=description,
            id=id,
            metadata=metadata,
            resume=resume,
        )

        return session_synthetic_body

