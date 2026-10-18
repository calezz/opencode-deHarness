from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_info_encoded_experimental_policies_item import ConfigInfoEncodedExperimentalPoliciesItem





T = TypeVar("T", bound="ConfigInfoEncodedExperimental")



@_attrs_define
class ConfigInfoEncodedExperimental:
    """ 
        Attributes:
            policies (list[ConfigInfoEncodedExperimentalPoliciesItem] | Unset):
            portable_shell_scanner (bool | Unset):
            subagent_depth (int | Unset):
     """

    policies: list[ConfigInfoEncodedExperimentalPoliciesItem] | Unset = UNSET
    portable_shell_scanner: bool | Unset = UNSET
    subagent_depth: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_info_encoded_experimental_policies_item import ConfigInfoEncodedExperimentalPoliciesItem # noqa: PLC0415
        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)



        portable_shell_scanner = self.portable_shell_scanner

        subagent_depth = self.subagent_depth


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if policies is not UNSET:
            field_dict["policies"] = policies
        if portable_shell_scanner is not UNSET:
            field_dict["portable_shell_scanner"] = portable_shell_scanner
        if subagent_depth is not UNSET:
            field_dict["subagent_depth"] = subagent_depth

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_info_encoded_experimental_policies_item import ConfigInfoEncodedExperimentalPoliciesItem # noqa: PLC0415
        d = dict(src_dict)
        _policies = d.pop("policies", UNSET)
        policies: list[ConfigInfoEncodedExperimentalPoliciesItem] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = ConfigInfoEncodedExperimentalPoliciesItem.from_dict(policies_item_data)



                policies.append(policies_item)


        portable_shell_scanner = d.pop("portable_shell_scanner", UNSET)

        subagent_depth = d.pop("subagent_depth", UNSET)

        config_info_encoded_experimental = cls(
            policies=policies,
            portable_shell_scanner=portable_shell_scanner,
            subagent_depth=subagent_depth,
        )

        return config_info_encoded_experimental

