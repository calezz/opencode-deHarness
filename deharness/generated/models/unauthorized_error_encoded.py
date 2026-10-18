from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.unauthorized_error_encoded_tag import UnauthorizedErrorEncodedTag






T = TypeVar("T", bound="UnauthorizedErrorEncoded")



@_attrs_define
class UnauthorizedErrorEncoded:
    """ 
        Attributes:
            field_tag (UnauthorizedErrorEncodedTag):
            message (str):
     """

    field_tag: UnauthorizedErrorEncodedTag
    message: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = UnauthorizedErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        unauthorized_error_encoded = cls(
            field_tag=field_tag,
            message=message,
        )

        return unauthorized_error_encoded

