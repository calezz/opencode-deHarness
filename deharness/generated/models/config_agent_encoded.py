from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.config_agent_encoded_mode import ConfigAgentEncodedMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_agent_encoded_model_type_1 import ConfigAgentEncodedModelType1
  from ..models.config_agent_encoded_request import ConfigAgentEncodedRequest
  from ..models.permission_rule import PermissionRule





T = TypeVar("T", bound="ConfigAgentEncoded")



@_attrs_define
class ConfigAgentEncoded:
    """ 
        Attributes:
            color (str | Unset):
            description (str | Unset):
            disabled (bool | Unset):
            hidden (bool | Unset):
            mode (ConfigAgentEncodedMode | Unset):
            model (ConfigAgentEncodedModelType1 | str | Unset):
            permissions (list[PermissionRule] | Unset):
            request (ConfigAgentEncodedRequest | Unset):
            steps (int | Unset):
            system (str | Unset):
     """

    color: str | Unset = UNSET
    description: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    hidden: bool | Unset = UNSET
    mode: ConfigAgentEncodedMode | Unset = UNSET
    model: ConfigAgentEncodedModelType1 | str | Unset = UNSET
    permissions: list[PermissionRule] | Unset = UNSET
    request: ConfigAgentEncodedRequest | Unset = UNSET
    steps: int | Unset = UNSET
    system: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_agent_encoded_model_type_1 import ConfigAgentEncodedModelType1 # noqa: PLC0415
        from ..models.config_agent_encoded_request import ConfigAgentEncodedRequest # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        color = self.color

        description = self.description

        disabled = self.disabled

        hidden = self.hidden

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value


        model: dict[str, Any] | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, ConfigAgentEncodedModelType1):
            model = self.model.to_dict()
        else:
            model = self.model

        permissions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for componentsschemas_permission_ruleset_item_data in self.permissions:
                componentsschemas_permission_ruleset_item = componentsschemas_permission_ruleset_item_data.to_dict()
                permissions.append(componentsschemas_permission_ruleset_item)



        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        steps = self.steps

        system = self.system


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if mode is not UNSET:
            field_dict["mode"] = mode
        if model is not UNSET:
            field_dict["model"] = model
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if request is not UNSET:
            field_dict["request"] = request
        if steps is not UNSET:
            field_dict["steps"] = steps
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_agent_encoded_model_type_1 import ConfigAgentEncodedModelType1 # noqa: PLC0415
        from ..models.config_agent_encoded_request import ConfigAgentEncodedRequest # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        d = dict(src_dict)
        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        disabled = d.pop("disabled", UNSET)

        hidden = d.pop("hidden", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: ConfigAgentEncodedMode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = ConfigAgentEncodedMode(_mode)




        def _parse_model(data: object) -> ConfigAgentEncodedModelType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_1 = ConfigAgentEncodedModelType1.from_dict(data)



                return model_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigAgentEncodedModelType1 | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        _permissions = d.pop("permissions", UNSET)
        permissions: list[PermissionRule] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for componentsschemas_permission_ruleset_item_data in _permissions:
                componentsschemas_permission_ruleset_item = PermissionRule.from_dict(componentsschemas_permission_ruleset_item_data)



                permissions.append(componentsschemas_permission_ruleset_item)


        _request = d.pop("request", UNSET)
        request: ConfigAgentEncodedRequest | Unset
        if isinstance(_request,  Unset):
            request = UNSET
        else:
            request = ConfigAgentEncodedRequest.from_dict(_request)




        steps = d.pop("steps", UNSET)

        system = d.pop("system", UNSET)

        config_agent_encoded = cls(
            color=color,
            description=description,
            disabled=disabled,
            hidden=hidden,
            mode=mode,
            model=model,
            permissions=permissions,
            request=request,
            steps=steps,
            system=system,
        )

        return config_agent_encoded

