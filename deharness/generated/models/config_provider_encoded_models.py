from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.config_model_encoded import ConfigModelEncoded





T = TypeVar("T", bound="ConfigProviderEncodedModels")



@_attrs_define
class ConfigProviderEncodedModels:
    

    additional_properties: dict[str, ConfigModelEncoded] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_model_encoded import ConfigModelEncoded # noqa: PLC0415
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_model_encoded import ConfigModelEncoded # noqa: PLC0415
        d = dict(src_dict)
        config_provider_encoded_models = cls(
        )


        from ..models.config_model_capabilities import ConfigModelCapabilities # noqa: PLC0415
        from ..models.config_model_cost_encoded import ConfigModelCostEncoded # noqa: PLC0415
        from ..models.config_model_encoded_body import ConfigModelEncodedBody # noqa: PLC0415
        from ..models.config_model_encoded_headers import ConfigModelEncodedHeaders # noqa: PLC0415
        from ..models.config_model_encoded_limit import ConfigModelEncodedLimit # noqa: PLC0415
        from ..models.config_model_encoded_variants_item import ConfigModelEncodedVariantsItem # noqa: PLC0415
        from ..models.config_model_settings import ConfigModelSettings # noqa: PLC0415
        from ..models.model_compatibility import ModelCompatibility # noqa: PLC0415
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ConfigModelEncoded.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        config_provider_encoded_models.additional_properties = additional_properties
        return config_provider_encoded_models

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ConfigModelEncoded:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ConfigModelEncoded) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
