from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef
  from ..models.pty import Pty





T = TypeVar("T", bound="PtyUpdateResponse200")



@_attrs_define
class PtyUpdateResponse200:
    """ 
        Attributes:
            data (Pty):
            location (LocationPublicRef):
     """

    data: Pty
    location: LocationPublicRef





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.pty import Pty # noqa: PLC0415
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
        from ..models.pty import Pty # noqa: PLC0415
        d = dict(src_dict)
        data = Pty.from_dict(d.pop("data"))




        location = LocationPublicRef.from_dict(d.pop("location"))




        pty_update_response_200 = cls(
            data=data,
            location=location,
        )

        return pty_update_response_200

