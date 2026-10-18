from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_model_reasoning_type_0 import ConfigModelReasoningType0
  from ..models.config_model_reasoning_type_1 import ConfigModelReasoningType1





T = TypeVar("T", bound="ConfigModelCapabilities")



@_attrs_define
class ConfigModelCapabilities:
    """ 
        Attributes:
            input_ (list[str] | Unset):
            output (list[str] | Unset):
            reasoning (ConfigModelReasoningType0 | ConfigModelReasoningType1 | Unset):
            temperature (bool | Unset):
            tools (bool | Unset):
     """

    input_: list[str] | Unset = UNSET
    output: list[str] | Unset = UNSET
    reasoning: ConfigModelReasoningType0 | ConfigModelReasoningType1 | Unset = UNSET
    temperature: bool | Unset = UNSET
    tools: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_model_reasoning_type_0 import ConfigModelReasoningType0 # noqa: PLC0415
        from ..models.config_model_reasoning_type_1 import ConfigModelReasoningType1 # noqa: PLC0415
        input_: list[str] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_



        output: list[str] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output



        reasoning: dict[str, Any] | Unset
        if isinstance(self.reasoning, Unset):
            reasoning = UNSET
        elif isinstance(self.reasoning, ConfigModelReasoningType0):
            reasoning = self.reasoning.to_dict()
        else:
            reasoning = self.reasoning.to_dict()


        temperature = self.temperature

        tools = self.tools


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_model_reasoning_type_0 import ConfigModelReasoningType0 # noqa: PLC0415
        from ..models.config_model_reasoning_type_1 import ConfigModelReasoningType1 # noqa: PLC0415
        d = dict(src_dict)
        input_ = cast(list[str], d.pop("input", UNSET))


        output = cast(list[str], d.pop("output", UNSET))


        def _parse_reasoning(data: object) -> ConfigModelReasoningType0 | ConfigModelReasoningType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_config_model_reasoning_type_0 = ConfigModelReasoningType0.from_dict(data)



                return componentsschemas_config_model_reasoning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_config_model_reasoning_type_1 = ConfigModelReasoningType1.from_dict(data)



            return componentsschemas_config_model_reasoning_type_1

        reasoning = _parse_reasoning(d.pop("reasoning", UNSET))


        temperature = d.pop("temperature", UNSET)

        tools = d.pop("tools", UNSET)

        config_model_capabilities = cls(
            input_=input_,
            output=output,
            reasoning=reasoning,
            temperature=temperature,
            tools=tools,
        )

        return config_model_capabilities

