from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.command_info import CommandInfo
  from ..models.location_public_ref import LocationPublicRef





T = TypeVar("T", bound="CommandListResponse200")



@_attrs_define
class CommandListResponse200:
    """ 
        Attributes:
            data (list[CommandInfo]):
            location (LocationPublicRef):
     """

    data: list[CommandInfo]
    location: LocationPublicRef





    def to_dict(self) -> dict[str, Any]:
        from ..models.command_info import CommandInfo # noqa: PLC0415
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        location = self.location.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "data": data,
            "location": location,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.command_info import CommandInfo # noqa: PLC0415
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = CommandInfo.from_dict(data_item_data)



            data.append(data_item)


        location = LocationPublicRef.from_dict(d.pop("location"))




        command_list_response_200 = cls(
            data=data,
            location=location,
        )

        return command_list_response_200

