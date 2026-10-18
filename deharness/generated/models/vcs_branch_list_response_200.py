from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef





T = TypeVar("T", bound="VcsBranchListResponse200")



@_attrs_define
class VcsBranchListResponse200:
    """ 
        Attributes:
            data (list[str]):
            location (LocationPublicRef):
     """

    data: list[str]
    location: LocationPublicRef





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        data = self.data



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
        d = dict(src_dict)
        data = cast(list[str], d.pop("data"))


        location = LocationPublicRef.from_dict(d.pop("location"))




        vcs_branch_list_response_200 = cls(
            data=data,
            location=location,
        )

        return vcs_branch_list_response_200

