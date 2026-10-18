from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.location_not_found_error_encoded_tag import LocationNotFoundErrorEncodedTag
from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef





T = TypeVar("T", bound="LocationNotFoundErrorEncoded")



@_attrs_define
class LocationNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (LocationNotFoundErrorEncodedTag):
            location (LocationPublicRef):
            message (str):
     """

    field_tag: LocationNotFoundErrorEncodedTag
    location: LocationPublicRef
    message: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        field_tag = self.field_tag.value

        location = self.location.to_dict()

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "location": location,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        d = dict(src_dict)
        field_tag = LocationNotFoundErrorEncodedTag(d.pop("_tag"))




        location = LocationPublicRef.from_dict(d.pop("location"))




        message = d.pop("message")

        location_not_found_error_encoded = cls(
            field_tag=field_tag,
            location=location,
            message=message,
        )

        return location_not_found_error_encoded

