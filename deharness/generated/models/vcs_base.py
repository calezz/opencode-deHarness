from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vcs_base_source import VcsBaseSource






T = TypeVar("T", bound="VcsBase")



@_attrs_define
class VcsBase:
    """ 
        Attributes:
            name (str):
            ref (str):
            source (VcsBaseSource):
     """

    name: str
    ref: str
    source: VcsBaseSource





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        ref = self.ref

        source = self.source.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "ref": ref,
            "source": source,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        ref = d.pop("ref")

        source = VcsBaseSource(d.pop("source"))




        vcs_base = cls(
            name=name,
            ref=ref,
            source=source,
        )

        return vcs_base

