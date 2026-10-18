from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectIcon")



@_attrs_define
class ProjectIcon:
    """ 
        Attributes:
            color (str | Unset):
            override (str | Unset):
            url (str | Unset):
     """

    color: str | Unset = UNSET
    override: str | Unset = UNSET
    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        color = self.color

        override = self.override

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if override is not UNSET:
            field_dict["override"] = override
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        override = d.pop("override", UNSET)

        url = d.pop("url", UNSET)

        project_icon = cls(
            color=color,
            override=override,
            url=url,
        )

        return project_icon

