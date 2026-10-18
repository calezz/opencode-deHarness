from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_boolean_field_type import FormBooleanFieldType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.form_when import FormWhen





T = TypeVar("T", bound="FormBooleanField")



@_attrs_define
class FormBooleanField:
    """ 
        Attributes:
            key (str):
            type_ (FormBooleanFieldType):
            default (bool | Unset):
            description (str | Unset):
            hidden (bool | Unset):
            required (bool | Unset):
            title (str | Unset):
            when (list[FormWhen] | Unset):
     """

    key: str
    type_: FormBooleanFieldType
    default: bool | Unset = UNSET
    description: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    required: bool | Unset = UNSET
    title: str | Unset = UNSET
    when: list[FormWhen] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_when import FormWhen # noqa: PLC0415
        key = self.key

        type_ = self.type_.value

        default = self.default

        description = self.description

        hidden = self.hidden

        required = self.required

        title = self.title

        when: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.when, Unset):
            when = []
            for when_item_data in self.when:
                when_item = when_item_data.to_dict()
                when.append(when_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "type": type_,
        })
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if required is not UNSET:
            field_dict["required"] = required
        if title is not UNSET:
            field_dict["title"] = title
        if when is not UNSET:
            field_dict["when"] = when

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_when import FormWhen # noqa: PLC0415
        d = dict(src_dict)
        key = d.pop("key")

        type_ = FormBooleanFieldType(d.pop("type"))




        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        required = d.pop("required", UNSET)

        title = d.pop("title", UNSET)

        _when = d.pop("when", UNSET)
        when: list[FormWhen] | Unset = UNSET
        if _when is not UNSET:
            when = []
            for when_item_data in _when:
                when_item = FormWhen.from_dict(when_item_data)



                when.append(when_item)


        form_boolean_field = cls(
            key=key,
            type_=type_,
            default=default,
            description=description,
            hidden=hidden,
            required=required,
            title=title,
            when=when,
        )

        return form_boolean_field

