from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ModelInfoLimit")



@_attrs_define
class ModelInfoLimit:
    """ 
        Attributes:
            context (int):
            output (int):
            input_ (int | Unset):
     """

    context: int
    output: int
    input_: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        context = self.context

        output = self.output

        input_ = self.input_


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "context": context,
            "output": output,
        })
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context = d.pop("context")

        output = d.pop("output")

        input_ = d.pop("input", UNSET)

        model_info_limit = cls(
            context=context,
            output=output,
            input_=input_,
        )

        return model_info_limit

