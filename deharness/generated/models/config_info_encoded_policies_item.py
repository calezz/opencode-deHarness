from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.config_info_encoded_policies_item_action import ConfigInfoEncodedPoliciesItemAction
from ..models.config_info_encoded_policies_item_effect import ConfigInfoEncodedPoliciesItemEffect






T = TypeVar("T", bound="ConfigInfoEncodedPoliciesItem")



@_attrs_define
class ConfigInfoEncodedPoliciesItem:
    """ 
        Attributes:
            action (ConfigInfoEncodedPoliciesItemAction):
            effect (ConfigInfoEncodedPoliciesItemEffect):
            resource (str):
     """

    action: ConfigInfoEncodedPoliciesItemAction
    effect: ConfigInfoEncodedPoliciesItemEffect
    resource: str





    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

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
        action = ConfigInfoEncodedPoliciesItemAction(d.pop("action"))




        effect = ConfigInfoEncodedPoliciesItemEffect(d.pop("effect"))




        resource = d.pop("resource")

        config_info_encoded_policies_item = cls(
            action=action,
            effect=effect,
            resource=resource,
        )

        return config_info_encoded_policies_item

