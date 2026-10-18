from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_integer_field_default_type_1 import FormIntegerFieldDefaultType1
from ..models.form_integer_field_maximum_type_1 import FormIntegerFieldMaximumType1
from ..models.form_integer_field_minimum_type_1 import FormIntegerFieldMinimumType1
from ..models.form_integer_field_type import FormIntegerFieldType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.form_when import FormWhen





T = TypeVar("T", bound="FormIntegerField")



@_attrs_define
class FormIntegerField:
    """ 
        Attributes:
            key (str):
            type_ (FormIntegerFieldType):
            default (float | FormIntegerFieldDefaultType1 | Unset):
            description (str | Unset):
            hidden (bool | Unset):
            maximum (float | FormIntegerFieldMaximumType1 | Unset):
            minimum (float | FormIntegerFieldMinimumType1 | Unset):
            required (bool | Unset):
            title (str | Unset):
            when (list[FormWhen] | Unset):
     """

    key: str
    type_: FormIntegerFieldType
    default: float | FormIntegerFieldDefaultType1 | Unset = UNSET
    description: str | Unset = UNSET
    hidden: bool | Unset = UNSET
    maximum: float | FormIntegerFieldMaximumType1 | Unset = UNSET
    minimum: float | FormIntegerFieldMinimumType1 | Unset = UNSET
    required: bool | Unset = UNSET
    title: str | Unset = UNSET
    when: list[FormWhen] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_when import FormWhen # noqa: PLC0415
        key = self.key

        type_ = self.type_.value

        default: float | str | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        elif isinstance(self.default, FormIntegerFieldDefaultType1):
            default = self.default.value
        else:
            default = self.default

        description = self.description

        hidden = self.hidden

        maximum: float | str | Unset
        if isinstance(self.maximum, Unset):
            maximum = UNSET
        elif isinstance(self.maximum, FormIntegerFieldMaximumType1):
            maximum = self.maximum.value
        else:
            maximum = self.maximum

        minimum: float | str | Unset
        if isinstance(self.minimum, Unset):
            minimum = UNSET
        elif isinstance(self.minimum, FormIntegerFieldMinimumType1):
            minimum = self.minimum.value
        else:
            minimum = self.minimum

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
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
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

        type_ = FormIntegerFieldType(d.pop("type"))




        def _parse_default(data: object) -> float | FormIntegerFieldDefaultType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_type_1 = FormIntegerFieldDefaultType1(data)



                return default_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | FormIntegerFieldDefaultType1 | Unset, data)

        default = _parse_default(d.pop("default", UNSET))


        description = d.pop("description", UNSET)

        hidden = d.pop("hidden", UNSET)

        def _parse_maximum(data: object) -> float | FormIntegerFieldMaximumType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maximum_type_1 = FormIntegerFieldMaximumType1(data)



                return maximum_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | FormIntegerFieldMaximumType1 | Unset, data)

        maximum = _parse_maximum(d.pop("maximum", UNSET))


        def _parse_minimum(data: object) -> float | FormIntegerFieldMinimumType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                minimum_type_1 = FormIntegerFieldMinimumType1(data)



                return minimum_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | FormIntegerFieldMinimumType1 | Unset, data)

        minimum = _parse_minimum(d.pop("minimum", UNSET))


        required = d.pop("required", UNSET)

        title = d.pop("title", UNSET)

        _when = d.pop("when", UNSET)
        when: list[FormWhen] | Unset = UNSET
        if _when is not UNSET:
            when = []
            for when_item_data in _when:
                when_item = FormWhen.from_dict(when_item_data)



                when.append(when_item)


        form_integer_field = cls(
            key=key,
            type_=type_,
            default=default,
            description=description,
            hidden=hidden,
            maximum=maximum,
            minimum=minimum,
            required=required,
            title=title,
            when=when,
        )

        return form_integer_field

