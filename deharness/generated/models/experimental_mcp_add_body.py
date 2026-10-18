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





T = TypeVar("T", bound="ExperimentalMcpAddBody")



@_attrs_define
class ExperimentalMcpAddBody:
    """ 
        Attributes:
            config (McpLocalConfigEncoded | McpRemoteConfigEncoded):
     """

    config: McpLocalConfigEncoded | McpRemoteConfigEncoded





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_local_config_encoded import McpLocalConfigEncoded # noqa: PLC0415
        from ..models.mcp_remote_config_encoded import McpRemoteConfigEncoded # noqa: PLC0415
        config: dict[str, Any]
        if isinstance(self.config, McpLocalConfigEncoded):
            config = self.config.to_dict()
        else:
            config = self.config.to_dict()



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "config": config,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_local_config_encoded import McpLocalConfigEncoded # noqa: PLC0415
        from ..models.mcp_remote_config_encoded import McpRemoteConfigEncoded # noqa: PLC0415
        d = dict(src_dict)
        def _parse_config(data: object) -> McpLocalConfigEncoded | McpRemoteConfigEncoded:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = McpLocalConfigEncoded.from_dict(data)



                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            config_type_1 = McpRemoteConfigEncoded.from_dict(data)



            return config_type_1

        config = _parse_config(d.pop("config"))


        experimental_mcp_add_body = cls(
            config=config,
        )

        return experimental_mcp_add_body

