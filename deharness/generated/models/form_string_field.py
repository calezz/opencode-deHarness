from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_string_field_format import FormStringFieldFormat
from ..models.form_string_field_type import FormStringFieldType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.form_option import FormOption
  from ..models.form_when import FormWhen





T = TypeVar("T", bound="FormStringField")



@_attrs_define
class FormStringField:
    """ 
        Attributes:
            key (str):
            type_ (FormStringFieldType):
            custom (bool | Unset):
            default (str | Unset):
            description (str | Unset):
            format_ (FormStringFieldFormat | Unset):
            hidden (bool | Unset):
            max_length (int | Unset):
            min_length (int | Unset):
            options (list[FormOption] | Unset):
            pattern (str | Unset):
            placeholder (str | Unset):
            required (bool | Unset):
            title (str | Unset):
            when (list[FormWhen] | Unset):
     """

    key: str
    type_: FormStringFieldType
    custom: bool | Unset = UNSET
    default: str | Unset = UNSET
    description: str | Unset = UNSET
    format_: FormStringFieldFormat | Unset = UNSET
    hidden: bool | Unset = UNSET
    max_length: int | Unset = UNSET
    min_length: int | Unset = UNSET
    options: list[FormOption] | Unset = UNSET
    pattern: str | Unset = UNSET
    placeholder: str | Unset = UNSET
    required: bool | Unset = UNSET
    title: str | Unset = UNSET
    when: list[FormWhen] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_option import FormOption # noqa: PLC0415
        from ..models.form_when import FormWhen # noqa: PLC0415
        key = self.key

        type_ = self.type_.value

        custom = self.custom

        default = self.default

        description = self.description

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value


        hidden = self.hidden

        max_length = self.max_length

        min_length = self.min_length

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)



        pattern = self.pattern

        placeholder = self.placeholder

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
        if custom is not UNSET:
            field_dict["custom"] = custom
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if format_ is not UNSET:
            field_dict["format"] = format_
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if options is not UNSET:
            field_dict["options"] = options
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
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

        type_ = FormStringFieldType(d.pop("type"))




        custom = d.pop("custom", UNSET)

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: FormStringFieldFormat | Unset
        if isinstance(_format_,  Unset):
            format_ = UNSET
        else:
            format_ = FormStringFieldFormat(_format_)




        hidden = d.pop("hidden", UNSET)

        max_length = d.pop("maxLength", UNSET)

        min_length = d.pop("minLength", UNSET)

        _options = d.pop("options", UNSET)
        options: list[FormOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = FormOption.from_dict(options_item_data)



                options.append(options_item)


        pattern = d.pop("pattern", UNSET)

        placeholder = d.pop("placeholder", UNSET)

        required = d.pop("required", UNSET)

        title = d.pop("title", UNSET)

        _when = d.pop("when", UNSET)
        when: list[FormWhen] | Unset = UNSET
        if _when is not UNSET:
            when = []
            for when_item_data in _when:
                when_item = FormWhen.from_dict(when_item_data)



                when.append(when_item)


        form_string_field = cls(
            key=key,
            type_=type_,
            custom=custom,
            default=default,
            description=description,
            format_=format_,
            hidden=hidden,
            max_length=max_length,
            min_length=min_length,
            options=options,
            pattern=pattern,
            placeholder=placeholder,
            required=required,
            title=title,
            when=when,
        )

        return form_string_field

