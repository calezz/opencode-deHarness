from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.reference_local_source_type import ReferenceLocalSourceType






T = TypeVar("T", bound="ReferenceLocalSource")



@_attrs_define
class ReferenceLocalSource:
    """ 
        Attributes:
            path (str):
            type_ (ReferenceLocalSourceType):
     """

    path: str
    type_: ReferenceLocalSourceType





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

        type_ = ReferenceLocalSourceType(d.pop("type"))




        reference_local_source = cls(
            path=path,
            type_=type_,
        )

        return reference_local_source

