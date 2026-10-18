from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ConfigInfoEncodedLspType1AdditionalPropertyType0")



@_attrs_define
class ConfigInfoEncodedLspType1AdditionalPropertyType0:
    """ 
        Attributes:
            disabled (bool):
     """

    disabled: bool





    def to_dict(self) -> dict[str, Any]:
        disabled = self.disabled


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "disabled": disabled,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disabled = d.pop("disabled")

        config_info_encoded_lsp_type_1_additional_property_type_0 = cls(
            disabled=disabled,
        )

        return config_info_encoded_lsp_type_1_additional_property_type_0

