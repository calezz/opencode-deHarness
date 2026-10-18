from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_system_entry_type import FileSystemEntryType






T = TypeVar("T", bound="FileSystemEntry")



@_attrs_define
class FileSystemEntry:
    """ 
        Attributes:
            path (str):
            type_ (FileSystemEntryType):
     """

    path: str
    type_: FileSystemEntryType





    def to_dict(self) -> dict[str, Any]:
        path = self.path

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "path": path,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        type_ = FileSystemEntryType(d.pop("type"))




        file_system_entry = cls(
            path=path,
            type_=type_,
        )

        return file_system_entry

