from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.location_public_ref import LocationPublicRef
  from ..models.model_info import ModelInfo





T = TypeVar("T", bound="ModelDefaultResponse200")



@_attrs_define
class ModelDefaultResponse200:
    """ 
        Attributes:
            data (ModelInfo | None):
            location (LocationPublicRef):
     """

    data: ModelInfo | None
    location: LocationPublicRef





    def to_dict(self) -> dict[str, Any]:
        from ..models.location_public_ref import LocationPublicRef # noqa: PLC0415
        from ..models.model_info import ModelInfo # noqa: PLC0415
        data: dict[str, Any] | None
        if isinstance(self.data, ModelInfo):
            data = self.data.to_dict()
        else:
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
        from ..models.model_info import ModelInfo # noqa: PLC0415
        d = dict(src_dict)
        def _parse_data(data: object) -> ModelInfo | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = ModelInfo.from_dict(data)



                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelInfo | None, data)

        data = _parse_data(d.pop("data"))


        location = LocationPublicRef.from_dict(d.pop("location"))




        model_default_response_200 = cls(
            data=data,
            location=location,
        )

        return model_default_response_200

