from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.form_state_type_0_status import FormStateType0Status






T = TypeVar("T", bound="FormStateType0")



@_attrs_define
class FormStateType0:
    """ 
        Attributes:
            status (FormStateType0Status):
     """

    status: FormStateType0Status





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = FormStateType0Status(d.pop("status"))




        form_state_type_0 = cls(
            status=status,
        )

        return form_state_type_0

