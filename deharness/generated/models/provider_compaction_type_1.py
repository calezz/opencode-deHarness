from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provider_compaction_type_1_type import ProviderCompactionType1Type






T = TypeVar("T", bound="ProviderCompactionType1")



@_attrs_define
class ProviderCompactionType1:
    """ 
        Attributes:
            type_ (ProviderCompactionType1Type):
     """

    type_: ProviderCompactionType1Type





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ProviderCompactionType1Type(d.pop("type"))




        provider_compaction_type_1 = cls(
            type_=type_,
        )

        return provider_compaction_type_1

