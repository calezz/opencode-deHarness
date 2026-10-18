from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="McpResourceTemplate")



@_attrs_define
class McpResourceTemplate:
    """ 
        Attributes:
            name (str):
            server (str):
            uri_template (str):
            description (str | Unset):
            mime_type (str | Unset):
     """

    name: str
    server: str
    uri_template: str
    description: str | Unset = UNSET
    mime_type: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        server = self.server

        uri_template = self.uri_template

        description = self.description

        mime_type = self.mime_type


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "server": server,
            "uriTemplate": uri_template,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        server = d.pop("server")

        uri_template = d.pop("uriTemplate")

        description = d.pop("description", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        mcp_resource_template = cls(
            name=name,
            server=server,
            uri_template=uri_template,
            description=description,
            mime_type=mime_type,
        )

        return mcp_resource_template

