from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_model_selected_type import SessionMessageModelSelectedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.model_ref import ModelRef
  from ..models.session_message_model_selected_metadata import SessionMessageModelSelectedMetadata
  from ..models.session_message_model_selected_time import SessionMessageModelSelectedTime





T = TypeVar("T", bound="SessionMessageModelSelected")



@_attrs_define
class SessionMessageModelSelected:
    """ 
        Attributes:
            id (str):
            model (ModelRef):
            time (SessionMessageModelSelectedTime):
            type_ (SessionMessageModelSelectedType):
            metadata (SessionMessageModelSelectedMetadata | Unset):
            previous (ModelRef | Unset):
     """

    id: str
    model: ModelRef
    time: SessionMessageModelSelectedTime
    type_: SessionMessageModelSelectedType
    metadata: SessionMessageModelSelectedMetadata | Unset = UNSET
    previous: ModelRef | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.session_message_model_selected_metadata import SessionMessageModelSelectedMetadata # noqa: PLC0415
        from ..models.session_message_model_selected_time import SessionMessageModelSelectedTime # noqa: PLC0415
        id = self.id

        model = self.model.to_dict()

        time = self.time.to_dict()

        type_ = self.type_.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        previous: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "model": model,
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
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.session_message_model_selected_metadata import SessionMessageModelSelectedMetadata # noqa: PLC0415
        from ..models.session_message_model_selected_time import SessionMessageModelSelectedTime # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        model = ModelRef.from_dict(d.pop("model"))




        time = SessionMessageModelSelectedTime.from_dict(d.pop("time"))




        type_ = SessionMessageModelSelectedType(d.pop("type"))




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageModelSelectedMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageModelSelectedMetadata.from_dict(_metadata)




        _previous = d.pop("previous", UNSET)
        previous: ModelRef | Unset
        if isinstance(_previous,  Unset):
            previous = UNSET
        else:
            previous = ModelRef.from_dict(_previous)




        session_message_model_selected = cls(
            id=id,
            model=model,
            time=time,
            type_=type_,
            metadata=metadata,
            previous=previous,
        )

        return session_message_model_selected

