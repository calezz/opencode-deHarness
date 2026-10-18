from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_value_type_1_type_1 import FormValueType1Type1
from typing import cast






T = TypeVar("T", bound="FormAnswer")



@_attrs_define
class FormAnswer:
    

    additional_properties: dict[str, bool | float | FormValueType1Type1 | list[str] | str] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            
            if isinstance(prop, FormValueType1Type1):
                field_dict[prop_name] = prop.value
            elif isinstance(prop, list):
                field_dict[prop_name] = prop


            else:
                field_dict[prop_name] = prop


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        form_answer = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            def _parse_additional_property(data: object) -> bool | float | FormValueType1Type1 | list[str] | str:
                try:
                    if not isinstance(data, str):
                        raise TypeError()
                    componentsschemas_form_value_type_1_type_1 = FormValueType1Type1(data)



                    return componentsschemas_form_value_type_1_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    componentsschemas_form_value_type_3 = cast(list[str], data)

                    return componentsschemas_form_value_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(bool | float | FormValueType1Type1 | list[str] | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        form_answer.additional_properties = additional_properties
        return form_answer

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> bool | float | FormValueType1Type1 | list[str] | str:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: bool | float | FormValueType1Type1 | list[str] | str) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
