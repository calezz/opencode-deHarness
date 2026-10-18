from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.integration_method_not_found_error_encoded_tag import IntegrationMethodNotFoundErrorEncodedTag






T = TypeVar("T", bound="IntegrationMethodNotFoundErrorEncoded")



@_attrs_define
class IntegrationMethodNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (IntegrationMethodNotFoundErrorEncodedTag):
            integration_id (str):
            message (str):
            method_id (str):
     """

    field_tag: IntegrationMethodNotFoundErrorEncodedTag
    integration_id: str
    message: str
    method_id: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        integration_id = self.integration_id

        message = self.message

        method_id = self.method_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "integrationID": integration_id,
            "message": message,
            "methodID": method_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = IntegrationMethodNotFoundErrorEncodedTag(d.pop("_tag"))




        integration_id = d.pop("integrationID")

        message = d.pop("message")

        method_id = d.pop("methodID")

        integration_method_not_found_error_encoded = cls(
            field_tag=field_tag,
            integration_id=integration_id,
            message=message,
            method_id=method_id,
        )

        return integration_method_not_found_error_encoded

