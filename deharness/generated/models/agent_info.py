from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.agent_info_mode import AgentInfoMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.model_ref import ModelRef
  from ..models.permission_rule import PermissionRule
  from ..models.provider_request import ProviderRequest





T = TypeVar("T", bound="AgentInfo")



@_attrs_define
class AgentInfo:
    """ 
        Attributes:
            hidden (bool):
            id (str):
            mode (AgentInfoMode):
            name (str):
            permissions (list[PermissionRule]):
            request (ProviderRequest):
            color (str | Unset):
            description (str | Unset):
            model (ModelRef | Unset):
            steps (int | Unset):
            system (str | Unset):
     """

    hidden: bool
    id: str
    mode: AgentInfoMode
    name: str
    permissions: list[PermissionRule]
    request: ProviderRequest
    color: str | Unset = UNSET
    description: str | Unset = UNSET
    model: ModelRef | Unset = UNSET
    steps: int | Unset = UNSET
    system: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        from ..models.provider_request import ProviderRequest # noqa: PLC0415
        hidden = self.hidden

        id = self.id

        mode = self.mode.value

        name = self.name

        permissions = []
        for componentsschemas_permission_ruleset_item_data in self.permissions:
            componentsschemas_permission_ruleset_item = componentsschemas_permission_ruleset_item_data.to_dict()
            permissions.append(componentsschemas_permission_ruleset_item)



        request = self.request.to_dict()

        color = self.color

        description = self.description

        model: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        steps = self.steps

        system = self.system


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "hidden": hidden,
            "id": id,
            "mode": mode,
            "name": name,
            "permissions": permissions,
            "request": request,
        })
        if color is not UNSET:
            field_dict["color"] = color
        if description is not UNSET:
            field_dict["description"] = description
        if model is not UNSET:
            field_dict["model"] = model
        if steps is not UNSET:
            field_dict["steps"] = steps
        if system is not UNSET:
            field_dict["system"] = system

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_ref import ModelRef # noqa: PLC0415
        from ..models.permission_rule import PermissionRule # noqa: PLC0415
        from ..models.provider_request import ProviderRequest # noqa: PLC0415
        d = dict(src_dict)
        hidden = d.pop("hidden")

        id = d.pop("id")

        mode = AgentInfoMode(d.pop("mode"))




        name = d.pop("name")

        permissions = []
        _permissions = d.pop("permissions")
        for componentsschemas_permission_ruleset_item_data in (_permissions):
            componentsschemas_permission_ruleset_item = PermissionRule.from_dict(componentsschemas_permission_ruleset_item_data)



            permissions.append(componentsschemas_permission_ruleset_item)


        request = ProviderRequest.from_dict(d.pop("request"))




        color = d.pop("color", UNSET)

        description = d.pop("description", UNSET)

        _model = d.pop("model", UNSET)
        model: ModelRef | Unset
        if isinstance(_model,  Unset):
            model = UNSET
        else:
            model = ModelRef.from_dict(_model)




        steps = d.pop("steps", UNSET)

        system = d.pop("system", UNSET)

        agent_info = cls(
            hidden=hidden,
            id=id,
            mode=mode,
            name=name,
            permissions=permissions,
            request=request,
            color=color,
            description=description,
            model=model,
            steps=steps,
            system=system,
        )

        return agent_info

