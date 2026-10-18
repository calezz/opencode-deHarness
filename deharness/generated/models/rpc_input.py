from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RpcInput")



@_attrs_define
class RpcInput:
    """ 
        Attributes:
            input_ (Any | Unset):
     """

    input_: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_ = d.pop("input", UNSET)

        rpc_input = cls(
            input_=input_,
        )

        return rpc_input

