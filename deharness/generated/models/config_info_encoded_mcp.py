from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_info_encoded_mcp_servers import ConfigInfoEncodedMcpServers
  from ..models.config_info_encoded_mcp_timeout import ConfigInfoEncodedMcpTimeout





T = TypeVar("T", bound="ConfigInfoEncodedMcp")



@_attrs_define
class ConfigInfoEncodedMcp:
    """ 
        Attributes:
            servers (ConfigInfoEncodedMcpServers | Unset):
            timeout (ConfigInfoEncodedMcpTimeout | Unset):
     """

    servers: ConfigInfoEncodedMcpServers | Unset = UNSET
    timeout: ConfigInfoEncodedMcpTimeout | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_info_encoded_mcp_servers import ConfigInfoEncodedMcpServers # noqa: PLC0415
        from ..models.config_info_encoded_mcp_timeout import ConfigInfoEncodedMcpTimeout # noqa: PLC0415
        servers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers.to_dict()

        timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timeout, Unset):
            timeout = self.timeout.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if servers is not UNSET:
            field_dict["servers"] = servers
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_info_encoded_mcp_servers import ConfigInfoEncodedMcpServers # noqa: PLC0415
        from ..models.config_info_encoded_mcp_timeout import ConfigInfoEncodedMcpTimeout # noqa: PLC0415
        d = dict(src_dict)
        _servers = d.pop("servers", UNSET)
        servers: ConfigInfoEncodedMcpServers | Unset
        if isinstance(_servers,  Unset):
            servers = UNSET
        else:
            servers = ConfigInfoEncodedMcpServers.from_dict(_servers)




        _timeout = d.pop("timeout", UNSET)
        timeout: ConfigInfoEncodedMcpTimeout | Unset
        if isinstance(_timeout,  Unset):
            timeout = UNSET
        else:
            timeout = ConfigInfoEncodedMcpTimeout.from_dict(_timeout)




        config_info_encoded_mcp = cls(
            servers=servers,
            timeout=timeout,
        )

        return config_info_encoded_mcp

