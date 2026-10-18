from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.config_reference_git_encoded import ConfigReferenceGitEncoded
  from ..models.config_reference_local_encoded import ConfigReferenceLocalEncoded





T = TypeVar("T", bound="ConfigInfoEncodedReferences")



@_attrs_define
class ConfigInfoEncodedReferences:
    

    additional_properties: dict[str, ConfigReferenceGitEncoded | ConfigReferenceLocalEncoded | str] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_reference_git_encoded import ConfigReferenceGitEncoded # noqa: PLC0415
        from ..models.config_reference_local_encoded import ConfigReferenceLocalEncoded # noqa: PLC0415
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, ConfigReferenceGitEncoded):
                field_dict[prop_name] = prop.to_dict()
            elif isinstance(prop, ConfigReferenceLocalEncoded):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_reference_git_encoded import ConfigReferenceGitEncoded # noqa: PLC0415
        from ..models.config_reference_local_encoded import ConfigReferenceLocalEncoded # noqa: PLC0415
        d = dict(src_dict)
        config_info_encoded_references = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> ConfigReferenceGitEncoded | ConfigReferenceLocalEncoded | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = ConfigReferenceGitEncoded.from_dict(data)



                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_2 = ConfigReferenceLocalEncoded.from_dict(data)



                    return additional_property_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(ConfigReferenceGitEncoded | ConfigReferenceLocalEncoded | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        config_info_encoded_references.additional_properties = additional_properties
        return config_info_encoded_references

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ConfigReferenceGitEncoded | ConfigReferenceLocalEncoded | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ConfigReferenceGitEncoded | ConfigReferenceLocalEncoded | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
