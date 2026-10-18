from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigInfoEncodedCompactionKeep")



@_attrs_define
class ConfigInfoEncodedCompactionKeep:
    """ 
        Attributes:
            tokens (int | Unset):
     """

    tokens: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        tokens = self.tokens


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tokens = d.pop("tokens", UNSET)

        config_info_encoded_compaction_keep = cls(
            tokens=tokens,
        )

        return config_info_encoded_compaction_keep

