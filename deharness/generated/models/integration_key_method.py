from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_key_method_type import IntegrationKeyMethodType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.form_boolean_field import FormBooleanField
  from ..models.form_external_field import FormExternalField
  from ..models.form_integer_field import FormIntegerField
  from ..models.form_multiselect_field import FormMultiselectField
  from ..models.form_number_field import FormNumberField
  from ..models.form_string_field import FormStringField





T = TypeVar("T", bound="IntegrationKeyMethod")



@_attrs_define
class IntegrationKeyMethod:
    """ 
        Attributes:
            type_ (IntegrationKeyMethodType):
            form (list[FormBooleanField | FormExternalField | FormIntegerField | FormMultiselectField | FormNumberField |
                FormStringField] | Unset):
            label (str | Unset):
     """

    type_: IntegrationKeyMethodType
    form: list[FormBooleanField | FormExternalField | FormIntegerField | FormMultiselectField | FormNumberField | FormStringField] | Unset = UNSET
    label: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_boolean_field import FormBooleanField # noqa: PLC0415
        from ..models.form_external_field import FormExternalField # noqa: PLC0415
        from ..models.form_integer_field import FormIntegerField # noqa: PLC0415
        from ..models.form_multiselect_field import FormMultiselectField # noqa: PLC0415
        from ..models.form_number_field import FormNumberField # noqa: PLC0415
        from ..models.form_string_field import FormStringField # noqa: PLC0415
        type_ = self.type_.value

        form: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.form, Unset):
            form = []
            for componentsschemas_form_fields_2_item_data in self.form:
                componentsschemas_form_fields_2_item: dict[str, Any]
                if isinstance(componentsschemas_form_fields_2_item_data, FormStringField):
                    componentsschemas_form_fields_2_item = componentsschemas_form_fields_2_item_data.to_dict()
                elif isinstance(componentsschemas_form_fields_2_item_data, FormNumberField):
                    componentsschemas_form_fields_2_item = componentsschemas_form_fields_2_item_data.to_dict()
                elif isinstance(componentsschemas_form_fields_2_item_data, FormIntegerField):
                    componentsschemas_form_fields_2_item = componentsschemas_form_fields_2_item_data.to_dict()
                elif isinstance(componentsschemas_form_fields_2_item_data, FormBooleanField):
                    componentsschemas_form_fields_2_item = componentsschemas_form_fields_2_item_data.to_dict()
                elif isinstance(componentsschemas_form_fields_2_item_data, FormMultiselectField):
                    componentsschemas_form_fields_2_item = componentsschemas_form_fields_2_item_data.to_dict()
                else:
                    componentsschemas_form_fields_2_item = componentsschemas_form_fields_2_item_data.to_dict()

                form.append(componentsschemas_form_fields_2_item)



        label = self.label


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })
        if form is not UNSET:
            field_dict["form"] = form
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_boolean_field import FormBooleanField # noqa: PLC0415
        from ..models.form_external_field import FormExternalField # noqa: PLC0415
        from ..models.form_integer_field import FormIntegerField # noqa: PLC0415
        from ..models.form_multiselect_field import FormMultiselectField # noqa: PLC0415
        from ..models.form_number_field import FormNumberField # noqa: PLC0415
        from ..models.form_string_field import FormStringField # noqa: PLC0415
        d = dict(src_dict)
        type_ = IntegrationKeyMethodType(d.pop("type"))




        _form = d.pop("form", UNSET)
        form: list[FormBooleanField | FormExternalField | FormIntegerField | FormMultiselectField | FormNumberField | FormStringField] | Unset = UNSET
        if _form is not UNSET:
            form = []
            for componentsschemas_form_fields_2_item_data in _form:
                def _parse_componentsschemas_form_fields_2_item(data: object) -> FormBooleanField | FormExternalField | FormIntegerField | FormMultiselectField | FormNumberField | FormStringField:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_form_field_type_0 = FormStringField.from_dict(data)



                        return componentsschemas_form_field_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_form_field_type_1 = FormNumberField.from_dict(data)



                        return componentsschemas_form_field_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_form_field_type_2 = FormIntegerField.from_dict(data)



                        return componentsschemas_form_field_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_form_field_type_3 = FormBooleanField.from_dict(data)



                        return componentsschemas_form_field_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_form_field_type_4 = FormMultiselectField.from_dict(data)



                        return componentsschemas_form_field_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_form_field_type_5 = FormExternalField.from_dict(data)



                    return componentsschemas_form_field_type_5

                componentsschemas_form_fields_2_item = _parse_componentsschemas_form_fields_2_item(componentsschemas_form_fields_2_item_data)

                form.append(componentsschemas_form_fields_2_item)


        label = d.pop("label", UNSET)

        integration_key_method = cls(
            type_=type_,
            form=form,
            label=label,
        )

        return integration_key_method

