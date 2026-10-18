from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ServerInfoPaths")



@_attrs_define
class ServerInfoPaths:
    """ 
        Attributes:
            tmp (str):
     """

    tmp: str





    def to_dict(self) -> dict[str, Any]:
        tmp = self.tmp


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "tmp": tmp,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tmp = d.pop("tmp")

        server_info_paths = cls(
            tmp=tmp,
        )

        return server_info_paths

