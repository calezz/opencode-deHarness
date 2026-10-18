from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ConfigInfoEncodedModelType1")



@_attrs_define
class ConfigInfoEncodedModelType1:
    """ 
        Attributes:
            model (str):
            provider_id (str):
            variant (str | Unset):
     """

    model: str
    provider_id: str
    variant: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        model = self.model

        provider_id = self.provider_id

        variant = self.variant


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "model": model,
            "providerID": provider_id,
        })
        if variant is not UNSET:
            field_dict["variant"] = variant

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        provider_id = d.pop("providerID")

        variant = d.pop("variant", UNSET)

        config_info_encoded_model_type_1 = cls(
            model=model,
            provider_id=provider_id,
            variant=variant,
        )

        return config_info_encoded_model_type_1

