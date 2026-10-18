from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_local_config_encoded import McpLocalConfigEncoded
  from ..models.mcp_remote_config_encoded import McpRemoteConfigEncoded





T = TypeVar("T", bound="ConfigInfoEncodedMcpServers")



@_attrs_define
class ConfigInfoEncodedMcpServers:
    

    additional_properties: dict[str, McpLocalConfigEncoded | McpRemoteConfigEncoded] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_local_config_encoded import McpLocalConfigEncoded # noqa: PLC0415
        from ..models.mcp_remote_config_encoded import McpRemoteConfigEncoded # noqa: PLC0415
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, McpLocalConfigEncoded):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()



        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_local_config_encoded import McpLocalConfigEncoded # noqa: PLC0415
        from ..models.mcp_remote_config_encoded import McpRemoteConfigEncoded # noqa: PLC0415
        d = dict(src_dict)
        config_info_encoded_mcp_servers = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> McpLocalConfigEncoded | McpRemoteConfigEncoded:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = McpLocalConfigEncoded.from_dict(data)



                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_1 = McpRemoteConfigEncoded.from_dict(data)



                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        config_info_encoded_mcp_servers.additional_properties = additional_properties
        return config_info_encoded_mcp_servers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> McpLocalConfigEncoded | McpRemoteConfigEncoded:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: McpLocalConfigEncoded | McpRemoteConfigEncoded) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
