from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ModelCapabilities")



@_attrs_define
class ModelCapabilities:
    """ 
        Attributes:
            input_ (list[str]):
            output (list[str]):
            tools (bool):
            temperature (bool | Unset):
     """

    input_: list[str]
    output: list[str]
    tools: bool
    temperature: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        input_ = self.input_



        output = self.output



        tools = self.tools

        temperature = self.temperature


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "input": input_,
            "output": output,
            "tools": tools,
        })
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_ = cast(list[str], d.pop("input"))


        output = cast(list[str], d.pop("output"))


        tools = d.pop("tools")

        temperature = d.pop("temperature", UNSET)

        model_capabilities = cls(
            input_=input_,
            output=output,
            tools=tools,
            temperature=temperature,
        )

        return model_capabilities

