from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mcp_local_config_encoded_type import McpLocalConfigEncodedType
from ..models.mcp_protocol import McpProtocol
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_local_config_encoded_environment import McpLocalConfigEncodedEnvironment
  from ..models.mcp_local_config_encoded_timeout import McpLocalConfigEncodedTimeout





T = TypeVar("T", bound="McpLocalConfigEncoded")



@_attrs_define
class McpLocalConfigEncoded:
    """ 
        Attributes:
            command (list[str]):
            type_ (McpLocalConfigEncodedType):
            codemode (bool | Unset):
            cwd (str | Unset):
            disabled (bool | Unset):
            environment (McpLocalConfigEncodedEnvironment | Unset):
            protocol (McpProtocol | Unset): MCP protocol negotiation. "legacy" (default) opens with the initialize handshake
                and speaks protocol revisions up to 2025-11-25. "auto" probes for the 2026-07-28 revision and falls back to
                legacy when the server does not support it. "2026-07-28" requires that revision and fails otherwise.
            timeout (McpLocalConfigEncodedTimeout | Unset):
     """

    command: list[str]
    type_: McpLocalConfigEncodedType
    codemode: bool | Unset = UNSET
    cwd: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    environment: McpLocalConfigEncodedEnvironment | Unset = UNSET
    protocol: McpProtocol | Unset = UNSET
    timeout: McpLocalConfigEncodedTimeout | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_local_config_encoded_environment import McpLocalConfigEncodedEnvironment # noqa: PLC0415
        from ..models.mcp_local_config_encoded_timeout import McpLocalConfigEncodedTimeout # noqa: PLC0415
        command = self.command



        type_ = self.type_.value

        codemode = self.codemode

        cwd = self.cwd

        disabled = self.disabled

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value


        timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timeout, Unset):
            timeout = self.timeout.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "command": command,
            "type": type_,
        })
        if codemode is not UNSET:
            field_dict["codemode"] = codemode
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if environment is not UNSET:
            field_dict["environment"] = environment
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_local_config_encoded_environment import McpLocalConfigEncodedEnvironment # noqa: PLC0415
        from ..models.mcp_local_config_encoded_timeout import McpLocalConfigEncodedTimeout # noqa: PLC0415
        d = dict(src_dict)
        command = cast(list[str], d.pop("command"))


        type_ = McpLocalConfigEncodedType(d.pop("type"))




        codemode = d.pop("codemode", UNSET)

        cwd = d.pop("cwd", UNSET)

        disabled = d.pop("disabled", UNSET)

        _environment = d.pop("environment", UNSET)
        environment: McpLocalConfigEncodedEnvironment | Unset
        if isinstance(_environment,  Unset):
            environment = UNSET
        else:
            environment = McpLocalConfigEncodedEnvironment.from_dict(_environment)




        _protocol = d.pop("protocol", UNSET)
        protocol: McpProtocol | Unset
        if isinstance(_protocol,  Unset):
            protocol = UNSET
        else:
            protocol = McpProtocol(_protocol)




        _timeout = d.pop("timeout", UNSET)
        timeout: McpLocalConfigEncodedTimeout | Unset
        if isinstance(_timeout,  Unset):
            timeout = UNSET
        else:
            timeout = McpLocalConfigEncodedTimeout.from_dict(_timeout)




        mcp_local_config_encoded = cls(
            command=command,
            type_=type_,
            codemode=codemode,
            cwd=cwd,
            disabled=disabled,
            environment=environment,
            protocol=protocol,
            timeout=timeout,
        )

        return mcp_local_config_encoded

