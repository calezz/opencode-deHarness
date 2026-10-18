from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="LocationPublicInfoProject")



@_attrs_define
class LocationPublicInfoProject:
    """ 
        Attributes:
            canonical (str):
            directory (str):
            id (str):
     """

    canonical: str
    directory: str
    id: str





    def to_dict(self) -> dict[str, Any]:
        canonical = self.canonical

        directory = self.directory

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "canonical": canonical,
            "directory": directory,
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        canonical = d.pop("canonical")

        directory = d.pop("directory")

        id = d.pop("id")

        location_public_info_project = cls(
            canonical=canonical,
            directory=directory,
            id=id,
        )

        return location_public_info_project

