from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef
  from ..models.web_search_provider import WebSearchProvider





T = TypeVar("T", bound="WebsearchProvidersResponse200")



@_attrs_define
class WebsearchProvidersResponse200:
    """ 
        Attributes:
            data (list[WebSearchProvider]):
            location (LocationPublicRef):
     """

    data: list[WebSearchProvider]
    location: LocationPublicRef





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.web_search_provider import WebSearchProvider # noqa: PLC0415
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
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.web_search_provider import WebSearchProvider # noqa: PLC0415
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = WebSearchProvider.from_dict(data_item_data)



            data.append(data_item)


        location = LocationPublicRef.from_dict(d.pop("location"))




        websearch_providers_response_200 = cls(
            data=data,
            location=location,
        )

        return websearch_providers_response_200

