from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.config_web_search_info_encoded_provider_type_0 import ConfigWebSearchInfoEncodedProviderType0
from typing import cast






T = TypeVar("T", bound="ConfigWebSearchInfoEncoded")



@_attrs_define
class ConfigWebSearchInfoEncoded:
    """ 
        Attributes:
            provider (ConfigWebSearchInfoEncodedProviderType0 | str):
     """

    provider: ConfigWebSearchInfoEncodedProviderType0 | str





    def to_dict(self) -> dict[str, Any]:
        provider: str
        if isinstance(self.provider, ConfigWebSearchInfoEncodedProviderType0):
            provider = self.provider.value
        else:
            provider = self.provider


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "provider": provider,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_provider(data: object) -> ConfigWebSearchInfoEncodedProviderType0 | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                provider_type_0 = ConfigWebSearchInfoEncodedProviderType0(data)



                return provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConfigWebSearchInfoEncodedProviderType0 | str, data)

        provider = _parse_provider(d.pop("provider"))


        config_web_search_info_encoded = cls(
            provider=provider,
        )

        return config_web_search_info_encoded

