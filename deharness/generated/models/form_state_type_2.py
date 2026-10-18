from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_state_type_2_status import FormStateType2Status
from ..types import UNSET, Unset






T = TypeVar("T", bound="FormStateType2")



@_attrs_define
class FormStateType2:
    """ 
        Attributes:
            status (FormStateType2Status):
            message (str | Unset):
     """

    status: FormStateType2Status
    message: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = FormStateType2Status(d.pop("status"))




        message = d.pop("message", UNSET)

        form_state_type_2 = cls(
            status=status,
            message=message,
        )

        return form_state_type_2

