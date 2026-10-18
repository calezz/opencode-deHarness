from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigModelEncodedLimit")



@_attrs_define
class ConfigModelEncodedLimit:
    """ 
        Attributes:
            context (int | Unset):
            input_ (int | Unset):
            output (int | Unset):
     """

    context: int | Unset = UNSET
    input_: int | Unset = UNSET
    output: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        context = self.context

        input_ = self.input_

        output = self.output


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if context is not UNSET:
            field_dict["context"] = context
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context = d.pop("context", UNSET)

        input_ = d.pop("input", UNSET)

        output = d.pop("output", UNSET)

        config_model_encoded_limit = cls(
            context=context,
            input_=input_,
            output=output,
        )

        return config_model_encoded_limit

