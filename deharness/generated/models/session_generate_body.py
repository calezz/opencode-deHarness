from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionGenerateBody")



@_attrs_define
class SessionGenerateBody:
    """ 
        Attributes:
            prompt (str):
     """

    prompt: str





    def to_dict(self) -> dict[str, Any]:
        prompt = self.prompt


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "prompt": prompt,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt = d.pop("prompt")

        session_generate_body = cls(
            prompt=prompt,
        )

        return session_generate_body

