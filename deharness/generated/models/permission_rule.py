from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.permission_effect import PermissionEffect






T = TypeVar("T", bound="PermissionRule")



@_attrs_define
class PermissionRule:
    """ 
        Attributes:
            action (str):
            effect (PermissionEffect):
            resource (str):
     """

    action: str
    effect: PermissionEffect
    resource: str





    def to_dict(self) -> dict[str, Any]:
        action = self.action

        effect = self.effect.value

        resource = self.resource


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "action": action,
            "effect": effect,
            "resource": resource,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        effect = PermissionEffect(d.pop("effect"))




        resource = d.pop("resource")

        permission_rule = cls(
            action=action,
            effect=effect,
            resource=resource,
        )

        return permission_rule

