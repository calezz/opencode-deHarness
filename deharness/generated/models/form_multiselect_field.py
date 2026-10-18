from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_multiselect_field_type import FormMultiselectFieldType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.form_option import FormOption
  from ..models.form_when import FormWhen





T = TypeVar("T", bound="FormMultiselectField")



@_attrs_define
class FormMultiselectField:
    """ 
        Attributes:
            key (str):
            options (list[FormOption]):
            type_ (FormMultiselectFieldType):
            custom (bool | Unset):
            default (list[str] | Unset):
            description (str | Unset):
            hidden (bool | Unset):
            max_items (int | Unset):
            min_items (int | Unset):
            required (bool | Unset):
            title (str | Unset):
            when (list[FormWhen] | Unset):
     """

    key: str
    options: list[FormOption]
    type_: FormMultiselectFieldType
    custom: bool | Unset = UNSET
    default: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    max_items: int | Unset = UNSET
    min_items: int | Unset = UNSET
    required: bool | Unset = UNSET
    title: str | Unset = UNSET
    when: list[FormWhen] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_option import FormOption # noqa: PLC0415
        from ..models.form_when import FormWhen # noqa: PLC0415
        key = self.key

        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)



        type_ = self.type_.value

        custom = self.custom

        default: list[str] | Unset = UNSET
        if not isinstance(self.default, Unset):
            default = self.default



        description = self.description

        hidden = self.hidden

        max_items = self.max_items

        min_items = self.min_items

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
            "options": options,
            "type": type_,
        })
        if custom is not UNSET:
            field_dict["custom"] = custom
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if min_items is not UNSET:
            field_dict["minItems"] = min_items
        if required is not UNSET:
            field_dict["required"] = required
        if title is not UNSET:
            field_dict["title"] = title
        if when is not UNSET:
            field_dict["when"] = when

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_option import FormOption # noqa: PLC0415
        from ..models.form_when import FormWhen # noqa: PLC0415
        d = dict(src_dict)
        key = d.pop("key")

        options = []
        _options = d.pop("options")
        for options_item_data in (_options):
            options_item = FormOption.from_dict(options_item_data)



            options.append(options_item)


        type_ = FormMultiselectFieldType(d.pop("type"))




        custom = d.pop("custom", UNSET)

        default = cast(list[str], d.pop("default", UNSET))


        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        max_items = d.pop("maxItems", UNSET)

        min_items = d.pop("minItems", UNSET)

        required = d.pop("required", UNSET)

        title = d.pop("title", UNSET)

        _when = d.pop("when", UNSET)
        when: list[FormWhen] | Unset = UNSET
        if _when is not UNSET:
            when = []
            for when_item_data in _when:
                when_item = FormWhen.from_dict(when_item_data)



                when.append(when_item)


        form_multiselect_field = cls(
            key=key,
            options=options,
            type_=type_,
            custom=custom,
            default=default,
            description=description,
            hidden=hidden,
            max_items=max_items,
            min_items=min_items,
            required=required,
            title=title,
            when=when,
        )

        return form_multiselect_field

