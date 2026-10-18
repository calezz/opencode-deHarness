from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RpcOutput")



@_attrs_define
class RpcOutput:
    """ 
        Attributes:
            output (Any | Unset):
     """

    output: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        output = self.output


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        output = d.pop("output", UNSET)

        rpc_output = cls(
            output=output,
        )

        return rpc_output

