from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.config_command_encoded import ConfigCommandEncoded





T = TypeVar("T", bound="ConfigInfoEncodedCommands")



@_attrs_define
class ConfigInfoEncodedCommands:
    

    additional_properties: dict[str, ConfigCommandEncoded] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_command_encoded import ConfigCommandEncoded # noqa: PLC0415
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_command_encoded import ConfigCommandEncoded # noqa: PLC0415
        d = dict(src_dict)
        config_info_encoded_commands = cls(
        )


        from ..models.config_command_encoded_model_type_1 import ConfigCommandEncodedModelType1 # noqa: PLC0415
        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ConfigCommandEncoded.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        config_info_encoded_commands.additional_properties = additional_properties
        return config_info_encoded_commands

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> ConfigCommandEncoded:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: ConfigCommandEncoded) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
