from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_not_found_error_encoded_tag import PermissionNotFoundErrorEncodedTag






T = TypeVar("T", bound="PermissionNotFoundErrorEncoded")



@_attrs_define
class PermissionNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (PermissionNotFoundErrorEncodedTag):
            message (str):
            request_id (str):
     """

    field_tag: PermissionNotFoundErrorEncodedTag
    message: str
    request_id: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        request_id = self.request_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "requestID": request_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = PermissionNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        request_id = d.pop("requestID")

        permission_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            request_id=request_id,
        )

        return permission_not_found_error_encoded

