from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_message_location_switched_type import SessionMessageLocationSwitchedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef
  from ..models.session_message_location_switched_metadata import SessionMessageLocationSwitchedMetadata
  from ..models.session_message_location_switched_previous_type_0 import SessionMessageLocationSwitchedPreviousType0
  from ..models.session_message_location_switched_time import SessionMessageLocationSwitchedTime





T = TypeVar("T", bound="SessionMessageLocationSwitched")



@_attrs_define
class SessionMessageLocationSwitched:
    """ 
        Attributes:
            id (str):
            location (LocationPublicRef):
            time (SessionMessageLocationSwitchedTime):
            type_ (SessionMessageLocationSwitchedType):
            metadata (SessionMessageLocationSwitchedMetadata | Unset):
            previous (None | SessionMessageLocationSwitchedPreviousType0 | Unset):
            project_id (str | Unset):
            subpath (str | Unset):
     """

    id: str
    location: LocationPublicRef
    time: SessionMessageLocationSwitchedTime
    type_: SessionMessageLocationSwitchedType
    metadata: SessionMessageLocationSwitchedMetadata | Unset = UNSET
    previous: None | SessionMessageLocationSwitchedPreviousType0 | Unset = UNSET
    project_id: str | Unset = UNSET
    subpath: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.session_message_location_switched_metadata import SessionMessageLocationSwitchedMetadata # noqa: PLC0415
        from ..models.session_message_location_switched_previous_type_0 import SessionMessageLocationSwitchedPreviousType0 # noqa: PLC0415
        from ..models.session_message_location_switched_time import SessionMessageLocationSwitchedTime # noqa: PLC0415
        id = self.id

        location = self.location.to_dict()

        time = self.time.to_dict()

        type_ = self.type_.value

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        previous: dict[str, Any] | None | Unset
        if isinstance(self.previous, Unset):
            previous = UNSET
        elif isinstance(self.previous, SessionMessageLocationSwitchedPreviousType0):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        project_id = self.project_id

        subpath = self.subpath


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "location": location,
            "time": time,
            "type": type_,
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if previous is not UNSET:
            field_dict["previous"] = previous
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if subpath is not UNSET:
            field_dict["subpath"] = subpath

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.session_message_location_switched_metadata import SessionMessageLocationSwitchedMetadata # noqa: PLC0415
        from ..models.session_message_location_switched_previous_type_0 import SessionMessageLocationSwitchedPreviousType0 # noqa: PLC0415
        from ..models.session_message_location_switched_time import SessionMessageLocationSwitchedTime # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        location = LocationPublicRef.from_dict(d.pop("location"))




        time = SessionMessageLocationSwitchedTime.from_dict(d.pop("time"))




        type_ = SessionMessageLocationSwitchedType(d.pop("type"))




        _metadata = d.pop("metadata", UNSET)
        metadata: SessionMessageLocationSwitchedMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = SessionMessageLocationSwitchedMetadata.from_dict(_metadata)




        def _parse_previous(data: object) -> None | SessionMessageLocationSwitchedPreviousType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = SessionMessageLocationSwitchedPreviousType0.from_dict(data)



                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SessionMessageLocationSwitchedPreviousType0 | Unset, data)

        previous = _parse_previous(d.pop("previous", UNSET))


        project_id = d.pop("projectID", UNSET)

        subpath = d.pop("subpath", UNSET)

        session_message_location_switched = cls(
            id=id,
            location=location,
            time=time,
            type_=type_,
            metadata=metadata,
            previous=previous,
            project_id=project_id,
            subpath=subpath,
        )

        return session_message_location_switched

