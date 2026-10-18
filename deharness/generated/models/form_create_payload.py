from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.form_boolean_field import FormBooleanField
  from ..models.form_external_field import FormExternalField
  from ..models.form_integer_field import FormIntegerField
  from ..models.form_metadata import FormMetadata
  from ..models.form_multiselect_field import FormMultiselectField
  from ..models.form_number_field import FormNumberField
  from ..models.form_string_field import FormStringField





T = TypeVar("T", bound="FormCreatePayload")



@_attrs_define
class FormCreatePayload:
    """ 
        Attributes:
            fields (list[FormBooleanField | FormExternalField | FormIntegerField | FormMultiselectField | FormNumberField |
                FormStringField]):
            title (str):
            id (None | str | Unset):
            metadata (FormMetadata | Unset):
     """

    fields: list[FormBooleanField | FormExternalField | FormIntegerField | FormMultiselectField | FormNumberField | FormStringField]
    title: str
    id: None | str | Unset = UNSET
    metadata: FormMetadata | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.form_boolean_field import FormBooleanField # noqa: PLC0415
        from ..models.form_external_field import FormExternalField # noqa: PLC0415
        from ..models.form_integer_field import FormIntegerField # noqa: PLC0415
        from ..models.form_metadata import FormMetadata # noqa: PLC0415
        from ..models.form_multiselect_field import FormMultiselectField # noqa: PLC0415
        from ..models.form_number_field import FormNumberField # noqa: PLC0415
        from ..models.form_string_field import FormStringField # noqa: PLC0415
        fields = []
        for componentsschemas_form_fields_item_data in self.fields:
            componentsschemas_form_fields_item: dict[str, Any]
            if isinstance(componentsschemas_form_fields_item_data, FormStringField):
                componentsschemas_form_fields_item = componentsschemas_form_fields_item_data.to_dict()
            elif isinstance(componentsschemas_form_fields_item_data, FormNumberField):
                componentsschemas_form_fields_item = componentsschemas_form_fields_item_data.to_dict()
            elif isinstance(componentsschemas_form_fields_item_data, FormIntegerField):
                componentsschemas_form_fields_item = componentsschemas_form_fields_item_data.to_dict()
            elif isinstance(componentsschemas_form_fields_item_data, FormBooleanField):
                componentsschemas_form_fields_item = componentsschemas_form_fields_item_data.to_dict()
            elif isinstance(componentsschemas_form_fields_item_data, FormMultiselectField):
                componentsschemas_form_fields_item = componentsschemas_form_fields_item_data.to_dict()
            else:
                componentsschemas_form_fields_item = componentsschemas_form_fields_item_data.to_dict()

            fields.append(componentsschemas_form_fields_item)



        title = self.title

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fields": fields,
            "title": title,
        })
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.form_boolean_field import FormBooleanField # noqa: PLC0415
        from ..models.form_external_field import FormExternalField # noqa: PLC0415
        from ..models.form_integer_field import FormIntegerField # noqa: PLC0415
        from ..models.form_metadata import FormMetadata # noqa: PLC0415
        from ..models.form_multiselect_field import FormMultiselectField # noqa: PLC0415
        from ..models.form_number_field import FormNumberField # noqa: PLC0415
        from ..models.form_string_field import FormStringField # noqa: PLC0415
        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for componentsschemas_form_fields_item_data in (_fields):
            def _parse_componentsschemas_form_fields_item(data: object) -> FormBooleanField | FormExternalField | FormIntegerField | FormMultiselectField | FormNumberField | FormStringField:
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

            componentsschemas_form_fields_item = _parse_componentsschemas_form_fields_item(componentsschemas_form_fields_item_data)

            fields.append(componentsschemas_form_fields_item)


        title = d.pop("title")

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        _metadata = d.pop("metadata", UNSET)
        metadata: FormMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = FormMetadata.from_dict(_metadata)




        form_create_payload = cls(
            fields=fields,
            title=title,
            id=id,
            metadata=metadata,
        )

        return form_create_payload

