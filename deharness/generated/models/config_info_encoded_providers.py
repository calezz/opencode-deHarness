from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.config_provider_encoded import ConfigProviderEncoded





T = TypeVar("T", bound="ConfigInfoEncodedProviders")



@_attrs_define
class ConfigInfoEncodedProviders:
    

    additional_properties: dict[str, ConfigProviderEncoded] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_provider_encoded import ConfigProviderEncoded # noqa: PLC0415
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_provider_encoded import ConfigProviderEncoded # noqa: PLC0415
        d = dict(src_dict)
        config_info_encoded_providers = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ConfigProviderEncoded.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        config_info_encoded_providers.additional_properties = additional_properties
        return config_info_encoded_providers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ConfigProviderEncoded:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ConfigProviderEncoded) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
