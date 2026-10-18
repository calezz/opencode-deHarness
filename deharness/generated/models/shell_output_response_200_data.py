from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ShellOutputResponse200Data")



@_attrs_define
class ShellOutputResponse200Data:
    """ 
        Attributes:
            cursor (int):
            output (str):
            size (int):
            truncated (bool):
     """

    cursor: int
    output: str
    size: int
    truncated: bool





    def to_dict(self) -> dict[str, Any]:
        cursor = self.cursor

        output = self.output

        size = self.size

        truncated = self.truncated


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "cursor": cursor,
            "output": output,
            "size": size,
            "truncated": truncated,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cursor = d.pop("cursor")

        output = d.pop("output")

        size = d.pop("size")

        truncated = d.pop("truncated")

        shell_output_response_200_data = cls(
            cursor=cursor,
            output=output,
            size=size,
            truncated=truncated,
        )

        return shell_output_response_200_data

