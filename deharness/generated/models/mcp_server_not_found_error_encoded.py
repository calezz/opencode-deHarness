from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mcp_server_not_found_error_encoded_tag import McpServerNotFoundErrorEncodedTag






T = TypeVar("T", bound="McpServerNotFoundErrorEncoded")



@_attrs_define
class McpServerNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (McpServerNotFoundErrorEncodedTag):
            message (str):
            server (str):
     """

    field_tag: McpServerNotFoundErrorEncodedTag
    message: str
    server: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        server = self.server


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "server": server,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = McpServerNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        server = d.pop("server")

        mcp_server_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            server=server,
        )

        return mcp_server_not_found_error_encoded

