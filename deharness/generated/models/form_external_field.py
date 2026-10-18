from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_external_field_type import FormExternalFieldType
from ..types import UNSET, Unset






T = TypeVar("T", bound="FormExternalField")



@_attrs_define
class FormExternalField:
    """ 
        Attributes:
            key (str):
            type_ (FormExternalFieldType):
            url (str):
            description (str | Unset):
            title (str | Unset):
     """

    key: str
    type_: FormExternalFieldType
    url: str
    description: str | Unset = UNSET
    title: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        type_ = self.type_.value

        url = self.url

        description = self.description

        title = self.title


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "type": type_,
            "url": url,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        type_ = FormExternalFieldType(d.pop("type"))




        url = d.pop("url")

        description = d.pop("description", UNSET)

        title = d.pop("title", UNSET)

        form_external_field = cls(
            key=key,
            type_=type_,
            url=url,
            description=description,
            title=title,
        )

        return form_external_field

