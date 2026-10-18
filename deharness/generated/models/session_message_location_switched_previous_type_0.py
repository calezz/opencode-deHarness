from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef





T = TypeVar("T", bound="SessionMessageLocationSwitchedPreviousType0")



@_attrs_define
class SessionMessageLocationSwitchedPreviousType0:
    """ 
        Attributes:
            location (LocationPublicRef):
            project_id (str | Unset):
            subpath (str | Unset):
     """

    location: LocationPublicRef
    project_id: str | Unset = UNSET
    subpath: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        location = self.location.to_dict()

        project_id = self.project_id

        subpath = self.subpath


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "location": location,
        })
        if project_id is not UNSET:
            field_dict["projectID"] = project_id
        if subpath is not UNSET:
            field_dict["subpath"] = subpath

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        d = dict(src_dict)
        location = LocationPublicRef.from_dict(d.pop("location"))




        project_id = d.pop("projectID", UNSET)

        subpath = d.pop("subpath", UNSET)

        session_message_location_switched_previous_type_0 = cls(
            location=location,
            project_id=project_id,
            subpath=subpath,
        )

        return session_message_location_switched_previous_type_0

