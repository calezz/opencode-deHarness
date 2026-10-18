from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_not_found_error_encoded_tag import FileNotFoundErrorEncodedTag






T = TypeVar("T", bound="FileNotFoundErrorEncoded")



@_attrs_define
class FileNotFoundErrorEncoded:
    """ 
        Attributes:
            field_tag (FileNotFoundErrorEncodedTag):
            message (str):
            path (str):
     """

    field_tag: FileNotFoundErrorEncodedTag
    message: str
    path: str





    def to_dict(self) -> dict[str, Any]:
        field_tag = self.field_tag.value

        message = self.message

        path = self.path


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "_tag": field_tag,
            "message": message,
            "path": path,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_tag = FileNotFoundErrorEncodedTag(d.pop("_tag"))




        message = d.pop("message")

        path = d.pop("path")

        file_not_found_error_encoded = cls(
            field_tag=field_tag,
            message=message,
            path=path,
        )

        return file_not_found_error_encoded

