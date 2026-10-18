from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PairingCode")



@_attrs_define
class PairingCode:
    """ 
        Attributes:
            code (str):
            expires_in (int):
     """

    code: str
    expires_in: int





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        expires_in = self.expires_in


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "expires_in": expires_in,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        expires_in = d.pop("expires_in")

        pairing_code = cls(
            code=code,
            expires_in=expires_in,
        )

        return pairing_code

