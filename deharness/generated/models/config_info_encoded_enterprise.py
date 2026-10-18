from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigInfoEncodedEnterprise")



@_attrs_define
class ConfigInfoEncodedEnterprise:
    """ 
        Attributes:
            url (str | Unset):
     """

    url: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        config_info_encoded_enterprise = cls(
            url=url,
        )

        return config_info_encoded_enterprise

