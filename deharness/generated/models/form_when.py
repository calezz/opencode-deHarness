from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_when_op import FormWhenOp
from ..models.form_when_value_type_1_type_1 import FormWhenValueType1Type1
from typing import cast






T = TypeVar("T", bound="FormWhen")



@_attrs_define
class FormWhen:
    """ 
        Attributes:
            key (str):
            op (FormWhenOp):
            value (bool | float | FormWhenValueType1Type1 | str):
     """

    key: str
    op: FormWhenOp
    value: bool | float | FormWhenValueType1Type1 | str





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        op = self.op.value

        value: bool | float | str
        if isinstance(self.value, FormWhenValueType1Type1):
            value = self.value.value
        else:
            value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "op": op,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        op = FormWhenOp(d.pop("op"))




        def _parse_value(data: object) -> bool | float | FormWhenValueType1Type1 | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                value_type_1_type_1 = FormWhenValueType1Type1(data)



                return value_type_1_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(bool | float | FormWhenValueType1Type1 | str, data)

        value = _parse_value(d.pop("value"))


        form_when = cls(
            key=key,
            op=op,
            value=value,
        )

        return form_when

