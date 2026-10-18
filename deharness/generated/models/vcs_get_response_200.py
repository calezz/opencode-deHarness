from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef
  from ..models.vcs_info import VcsInfo





T = TypeVar("T", bound="VcsGetResponse200")



@_attrs_define
class VcsGetResponse200:
    """ 
        Attributes:
            data (VcsInfo):
            location (LocationPublicRef):
     """

    data: VcsInfo
    location: LocationPublicRef





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.vcs_info import VcsInfo # noqa: PLC0415
        data = self.data.to_dict()

        location = self.location.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "location": location,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.vcs_info import VcsInfo # noqa: PLC0415
        d = dict(src_dict)
        data = VcsInfo.from_dict(d.pop("data"))




        location = LocationPublicRef.from_dict(d.pop("location"))




        vcs_get_response_200 = cls(
            data=data,
            location=location,
        )

        return vcs_get_response_200

