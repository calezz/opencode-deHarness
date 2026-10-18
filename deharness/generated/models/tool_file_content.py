from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tool_file_content_type import ToolFileContentType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ToolFileContent")



@_attrs_define
class ToolFileContent:
    """ 
        Attributes:
            mime (str):
            type_ (ToolFileContentType):
            uri (str):
            name (None | str | Unset):
     """

    mime: str
    type_: ToolFileContentType
    uri: str
    name: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        mime = self.mime

        type_ = self.type_.value

        uri = self.uri

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "mime": mime,
            "type": type_,
            "uri": uri,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mime = d.pop("mime")

        type_ = ToolFileContentType(d.pop("type"))




        uri = d.pop("uri")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        tool_file_content = cls(
            mime=mime,
            type_=type_,
            uri=uri,
            name=name,
        )

        return tool_file_content

