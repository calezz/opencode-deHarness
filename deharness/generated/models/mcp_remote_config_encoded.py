from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mcp_protocol import McpProtocol
from ..models.mcp_remote_config_encoded_type import McpRemoteConfigEncodedType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mcp_o_auth_config_encoded import McpOAuthConfigEncoded
  from ..models.mcp_remote_config_encoded_headers import McpRemoteConfigEncodedHeaders
  from ..models.mcp_remote_config_encoded_timeout import McpRemoteConfigEncodedTimeout





T = TypeVar("T", bound="McpRemoteConfigEncoded")



@_attrs_define
class McpRemoteConfigEncoded:
    """ 
        Attributes:
            type_ (McpRemoteConfigEncodedType):
            url (str):
            codemode (bool | Unset):
            disabled (bool | Unset):
            headers (McpRemoteConfigEncodedHeaders | Unset):
            oauth (bool | McpOAuthConfigEncoded | Unset):
            protocol (McpProtocol | Unset): MCP protocol negotiation. "legacy" (default) opens with the initialize handshake
                and speaks protocol revisions up to 2025-11-25. "auto" probes for the 2026-07-28 revision and falls back to
                legacy when the server does not support it. "2026-07-28" requires that revision and fails otherwise.
            timeout (McpRemoteConfigEncodedTimeout | Unset):
     """

    type_: McpRemoteConfigEncodedType
    url: str
    codemode: bool | Unset = UNSET
    disabled: bool | Unset = UNSET
    headers: McpRemoteConfigEncodedHeaders | Unset = UNSET
    oauth: bool | McpOAuthConfigEncoded | Unset = UNSET
    protocol: McpProtocol | Unset = UNSET
    timeout: McpRemoteConfigEncodedTimeout | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_o_auth_config_encoded import McpOAuthConfigEncoded # noqa: PLC0415
        from ..models.mcp_remote_config_encoded_headers import McpRemoteConfigEncodedHeaders # noqa: PLC0415
        from ..models.mcp_remote_config_encoded_timeout import McpRemoteConfigEncodedTimeout # noqa: PLC0415
        type_ = self.type_.value

        url = self.url

        codemode = self.codemode

        disabled = self.disabled

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        oauth: bool | dict[str, Any] | Unset
        if isinstance(self.oauth, Unset):
            oauth = UNSET
        elif isinstance(self.oauth, McpOAuthConfigEncoded):
            oauth = self.oauth.to_dict()
        else:
            oauth = self.oauth

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value


        timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timeout, Unset):
            timeout = self.timeout.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
            "url": url,
        })
        if codemode is not UNSET:
            field_dict["codemode"] = codemode
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if headers is not UNSET:
            field_dict["headers"] = headers
        if oauth is not UNSET:
            field_dict["oauth"] = oauth
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if timeout is not UNSET:
            field_dict["timeout"] = timeout

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_o_auth_config_encoded import McpOAuthConfigEncoded # noqa: PLC0415
        from ..models.mcp_remote_config_encoded_headers import McpRemoteConfigEncodedHeaders # noqa: PLC0415
        from ..models.mcp_remote_config_encoded_timeout import McpRemoteConfigEncodedTimeout # noqa: PLC0415
        d = dict(src_dict)
        type_ = McpRemoteConfigEncodedType(d.pop("type"))




        url = d.pop("url")

        codemode = d.pop("codemode", UNSET)

        disabled = d.pop("disabled", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: McpRemoteConfigEncodedHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = McpRemoteConfigEncodedHeaders.from_dict(_headers)




        def _parse_oauth(data: object) -> bool | McpOAuthConfigEncoded | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                oauth_type_0 = McpOAuthConfigEncoded.from_dict(data)



                return oauth_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | McpOAuthConfigEncoded | Unset, data)

        oauth = _parse_oauth(d.pop("oauth", UNSET))


        _protocol = d.pop("protocol", UNSET)
        protocol: McpProtocol | Unset
        if isinstance(_protocol,  Unset):
            protocol = UNSET
        else:
            protocol = McpProtocol(_protocol)




        _timeout = d.pop("timeout", UNSET)
        timeout: McpRemoteConfigEncodedTimeout | Unset
        if isinstance(_timeout,  Unset):
            timeout = UNSET
        else:
            timeout = McpRemoteConfigEncodedTimeout.from_dict(_timeout)




        mcp_remote_config_encoded = cls(
            type_=type_,
            url=url,
            codemode=codemode,
            disabled=disabled,
            headers=headers,
            oauth=oauth,
            protocol=protocol,
            timeout=timeout,
        )

        return mcp_remote_config_encoded

