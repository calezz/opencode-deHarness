from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="McpOAuthConfigEncoded")



@_attrs_define
class McpOAuthConfigEncoded:
    """ 
        Attributes:
            auth_server_metadata_url (str | Unset):
            callback_port (int | Unset):
            client_id (str | Unset):
            client_secret (str | Unset):
            redirect_uri (str | Unset):
            scope (str | Unset):
     """

    auth_server_metadata_url: str | Unset = UNSET
    callback_port: int | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    redirect_uri: str | Unset = UNSET
    scope: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        auth_server_metadata_url = self.auth_server_metadata_url

        callback_port = self.callback_port

        client_id = self.client_id

        client_secret = self.client_secret

        redirect_uri = self.redirect_uri

        scope = self.scope


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if auth_server_metadata_url is not UNSET:
            field_dict["auth_server_metadata_url"] = auth_server_metadata_url
        if callback_port is not UNSET:
            field_dict["callback_port"] = callback_port
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_server_metadata_url = d.pop("auth_server_metadata_url", UNSET)

        callback_port = d.pop("callback_port", UNSET)

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        redirect_uri = d.pop("redirect_uri", UNSET)

        scope = d.pop("scope", UNSET)

        mcp_o_auth_config_encoded = cls(
            auth_server_metadata_url=auth_server_metadata_url,
            callback_port=callback_port,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
            scope=scope,
        )

        return mcp_o_auth_config_encoded

