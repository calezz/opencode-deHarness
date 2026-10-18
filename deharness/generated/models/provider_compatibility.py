from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.model_cache_format import ModelCacheFormat
from ..models.model_max_tokens_field import ModelMaxTokensField
from ..models.model_reasoning_field_type_0 import ModelReasoningFieldType0
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ProviderCompatibility")



@_attrs_define
class ProviderCompatibility:
    """ 
        Attributes:
            cache_format (ModelCacheFormat | Unset):
            max_tokens_field (ModelMaxTokensField | Unset):
            reasoning_field (ModelReasoningFieldType0 | str | Unset):
            require_assistant_after_tool (bool | Unset):
            require_finish_reason (bool | Unset):
            require_reasoning (bool | Unset):
            supports_prompt_cache_key (bool | Unset):
     """

    cache_format: ModelCacheFormat | Unset = UNSET
    max_tokens_field: ModelMaxTokensField | Unset = UNSET
    reasoning_field: ModelReasoningFieldType0 | str | Unset = UNSET
    require_assistant_after_tool: bool | Unset = UNSET
    require_finish_reason: bool | Unset = UNSET
    require_reasoning: bool | Unset = UNSET
    supports_prompt_cache_key: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        cache_format: str | Unset = UNSET
        if not isinstance(self.cache_format, Unset):
            cache_format = self.cache_format.value


        max_tokens_field: str | Unset = UNSET
        if not isinstance(self.max_tokens_field, Unset):
            max_tokens_field = self.max_tokens_field.value


        reasoning_field: str | Unset
        if isinstance(self.reasoning_field, Unset):
            reasoning_field = UNSET
        elif isinstance(self.reasoning_field, ModelReasoningFieldType0):
            reasoning_field = self.reasoning_field.value
        else:
            reasoning_field = self.reasoning_field

        require_assistant_after_tool = self.require_assistant_after_tool

        require_finish_reason = self.require_finish_reason

        require_reasoning = self.require_reasoning

        supports_prompt_cache_key = self.supports_prompt_cache_key


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cache_format is not UNSET:
            field_dict["cacheFormat"] = cache_format
        if max_tokens_field is not UNSET:
            field_dict["maxTokensField"] = max_tokens_field
        if reasoning_field is not UNSET:
            field_dict["reasoningField"] = reasoning_field
        if require_assistant_after_tool is not UNSET:
            field_dict["requireAssistantAfterTool"] = require_assistant_after_tool
        if require_finish_reason is not UNSET:
            field_dict["requireFinishReason"] = require_finish_reason
        if require_reasoning is not UNSET:
            field_dict["requireReasoning"] = require_reasoning
        if supports_prompt_cache_key is not UNSET:
            field_dict["supportsPromptCacheKey"] = supports_prompt_cache_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _cache_format = d.pop("cacheFormat", UNSET)
        cache_format: ModelCacheFormat | Unset
        if isinstance(_cache_format,  Unset):
            cache_format = UNSET
        else:
            cache_format = ModelCacheFormat(_cache_format)




        _max_tokens_field = d.pop("maxTokensField", UNSET)
        max_tokens_field: ModelMaxTokensField | Unset
        if isinstance(_max_tokens_field,  Unset):
            max_tokens_field = UNSET
        else:
            max_tokens_field = ModelMaxTokensField(_max_tokens_field)




        def _parse_reasoning_field(data: object) -> ModelReasoningFieldType0 | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_model_reasoning_field_type_0 = ModelReasoningFieldType0(data)



                return componentsschemas_model_reasoning_field_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelReasoningFieldType0 | str | Unset, data)

        reasoning_field = _parse_reasoning_field(d.pop("reasoningField", UNSET))


        require_assistant_after_tool = d.pop("requireAssistantAfterTool", UNSET)

        require_finish_reason = d.pop("requireFinishReason", UNSET)

        require_reasoning = d.pop("requireReasoning", UNSET)

        supports_prompt_cache_key = d.pop("supportsPromptCacheKey", UNSET)

        provider_compatibility = cls(
            cache_format=cache_format,
            max_tokens_field=max_tokens_field,
            reasoning_field=reasoning_field,
            require_assistant_after_tool=require_assistant_after_tool,
            require_finish_reason=require_finish_reason,
            require_reasoning=require_reasoning,
            supports_prompt_cache_key=supports_prompt_cache_key,
        )

        return provider_compatibility

