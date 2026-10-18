from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SkillInfo")



@_attrs_define
class SkillInfo:
    """ 
        Attributes:
            content (str):
            id (str):
            name (str):
            path (str):
            autoinvoke (bool | Unset):
            description (str | Unset):
     """

    content: str
    id: str
    name: str
    path: str
    autoinvoke: bool | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        content = self.content

        id = self.id

        name = self.name

        path = self.path

        autoinvoke = self.autoinvoke

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "content": content,
            "id": id,
            "name": name,
            "path": path,
        })
        if autoinvoke is not UNSET:
            field_dict["autoinvoke"] = autoinvoke
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        id = d.pop("id")

        name = d.pop("name")

        path = d.pop("path")

        autoinvoke = d.pop("autoinvoke", UNSET)

        description = d.pop("description", UNSET)

        skill_info = cls(
            content=content,
            id=id,
            name=name,
            path=path,
            autoinvoke=autoinvoke,
            description=description,
        )

        return skill_info

