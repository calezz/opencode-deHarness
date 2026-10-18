from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provider_not_found_error_encoded_tag import ProviderNotFoundErrorEncodedTag






T = TypeVar("T", bound="ProviderNotFoundErrorEncoded")



@_attrs_define
class ProviderNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (ProviderNotFoundErrorEncodedTag):
            message (str):
            provider_id (str):
     """

    field_tag: ProviderNotFoundErrorEncodedTag
    message: str
    provider_id: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        provider_id = self.provider_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "providerID": provider_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = ProviderNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        provider_id = d.pop("providerID")

        provider_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            provider_id=provider_id,
        )

        return provider_not_found_error_encoded

