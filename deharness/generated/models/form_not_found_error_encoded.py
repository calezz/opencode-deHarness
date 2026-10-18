from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_not_found_error_encoded_tag import FormNotFoundErrorEncodedTag






T = TypeVar("T", bound="FormNotFoundErrorEncoded")



@_attrs_define
class FormNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (FormNotFoundErrorEncodedTag):
            id (str):
            message (str):
     """

    field_tag: FormNotFoundErrorEncodedTag
    id: str
    message: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        id = self.id

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "id": id,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = FormNotFoundErrorEncodedTag(d.pop("_tag"))




        id = d.pop("id")

        message = d.pop("message")

        form_not_found_error_encoded = cls(
            field_tag=field_tag,
            id=id,
            message=message,
        )

        return form_not_found_error_encoded

