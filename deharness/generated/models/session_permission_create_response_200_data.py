from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_effect import PermissionEffect






T = TypeVar("T", bound="SessionPermissionCreateResponse200Data")



@_attrs_define
class SessionPermissionCreateResponse200Data:
    """ 
        Attributes:
            effect (PermissionEffect):
            id (str):
     """

    effect: PermissionEffect
    id: str





    def to_dict(self) -> dict[str, Any]:
        effect = self.effect.value

        id = self.id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "effect": effect,
            "id": id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        effect = PermissionEffect(d.pop("effect"))




        id = d.pop("id")

        session_permission_create_response_200_data = cls(
            effect=effect,
            id=id,
        )

        return session_permission_create_response_200_data

