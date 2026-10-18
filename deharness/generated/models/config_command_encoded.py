from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_command_encoded_model_type_1 import ConfigCommandEncodedModelType1





T = TypeVar("T", bound="ConfigCommandEncoded")



@_attrs_define
class ConfigCommandEncoded:
    """ 
        Attributes:
            template (str):
            agent (str | Unset):
            description (str | Unset):
            model (ConfigCommandEncodedModelType1 | str | Unset):
            subagent (bool | Unset):
            subtask (bool | Unset): Deprecated alias for subagent.
     """

    template: str
    agent: str | Unset = UNSET
    description: str | Unset = UNSET
    model: ConfigCommandEncodedModelType1 | str | Unset = UNSET
    subagent: bool | Unset = UNSET
    subtask: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_command_encoded_model_type_1 import ConfigCommandEncodedModelType1 # noqa: PLC0415
        template = self.template

        agent = self.agent

        description = self.description

        model: dict[str, Any] | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        elif isinstance(self.model, ConfigCommandEncodedModelType1):
            model = self.model.to_dict()
        else:
            model = self.model

        subagent = self.subagent

        subtask = self.subtask


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "template": template,
        })
        if agent is not UNSET:
            field_dict["agent"] = agent
        if description is not UNSET:
            field_dict["description"] = description
        if model is not UNSET:
            field_dict["model"] = model
        if subagent is not UNSET:
            field_dict["subagent"] = subagent
        if subtask is not UNSET:
            field_dict["subtask"] = subtask

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_command_encoded_model_type_1 import ConfigCommandEncodedModelType1 # noqa: PLC0415
        d = dict(src_dict)
        template = d.pop("template")

        agent = d.pop("agent", UNSET)

        description = d.pop("description", UNSET)

        def _parse_model(data: object) -> ConfigCommandEncodedModelType1 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_type_1 = ConfigCommandEncodedModelType1.from_dict(data)



                return model_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigCommandEncodedModelType1 | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))


        subagent = d.pop("subagent", UNSET)

        subtask = d.pop("subtask", UNSET)

        config_command_encoded = cls(
            template=template,
            agent=agent,
            description=description,
            model=model,
            subagent=subagent,
            subtask=subtask,
        )

        return config_command_encoded

