from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_provider_encoded_body import ConfigProviderEncodedBody
  from ..models.config_provider_encoded_headers import ConfigProviderEncodedHeaders
  from ..models.config_provider_encoded_models import ConfigProviderEncodedModels
  from ..models.config_provider_settings import ConfigProviderSettings
  from ..models.provider_compatibility import ProviderCompatibility





T = TypeVar("T", bound="ConfigProviderEncoded")



@_attrs_define
class ConfigProviderEncoded:
    """ 
        Attributes:
            body (ConfigProviderEncodedBody | Unset):
            canonical (str | Unset):
            compatibility (ProviderCompatibility | Unset):
            env (list[str] | Unset):
            headers (ConfigProviderEncodedHeaders | Unset):
            models (ConfigProviderEncodedModels | Unset):
            name (str | Unset):
            package (str | Unset):
            settings (ConfigProviderSettings | Unset):
     """

    body: ConfigProviderEncodedBody | Unset = UNSET
    canonical: str | Unset = UNSET
    compatibility: ProviderCompatibility | Unset = UNSET
    env: list[str] | Unset = UNSET
    headers: ConfigProviderEncodedHeaders | Unset = UNSET
    models: ConfigProviderEncodedModels | Unset = UNSET
    name: str | Unset = UNSET
    package: str | Unset = UNSET
    settings: ConfigProviderSettings | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_provider_encoded_body import ConfigProviderEncodedBody # noqa: PLC0415
        from ..models.config_provider_encoded_headers import ConfigProviderEncodedHeaders # noqa: PLC0415
        from ..models.config_provider_encoded_models import ConfigProviderEncodedModels # noqa: PLC0415
        from ..models.config_provider_settings import ConfigProviderSettings # noqa: PLC0415
        from ..models.provider_compatibility import ProviderCompatibility # noqa: PLC0415
        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        canonical = self.canonical

        compatibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compatibility, Unset):
            compatibility = self.compatibility.to_dict()

        env: list[str] | Unset = UNSET
        if not isinstance(self.env, Unset):
            env = self.env



        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        models: dict[str, Any] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = self.models.to_dict()

        name = self.name

        package = self.package

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if body is not UNSET:
            field_dict["body"] = body
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility
        if env is not UNSET:
            field_dict["env"] = env
        if headers is not UNSET:
            field_dict["headers"] = headers
        if models is not UNSET:
            field_dict["models"] = models
        if name is not UNSET:
            field_dict["name"] = name
        if package is not UNSET:
            field_dict["package"] = package
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_provider_encoded_body import ConfigProviderEncodedBody # noqa: PLC0415
        from ..models.config_provider_encoded_headers import ConfigProviderEncodedHeaders # noqa: PLC0415
        from ..models.config_provider_encoded_models import ConfigProviderEncodedModels # noqa: PLC0415
        from ..models.config_provider_settings import ConfigProviderSettings # noqa: PLC0415
        from ..models.provider_compatibility import ProviderCompatibility # noqa: PLC0415
        d = dict(src_dict)
        _body = d.pop("body", UNSET)
        body: ConfigProviderEncodedBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = ConfigProviderEncodedBody.from_dict(_body)




        canonical = d.pop("canonical", UNSET)

        _compatibility = d.pop("compatibility", UNSET)
        compatibility: ProviderCompatibility | Unset
        if isinstance(_compatibility,  Unset):
            compatibility = UNSET
        else:
            compatibility = ProviderCompatibility.from_dict(_compatibility)




        env = cast(list[str], d.pop("env", UNSET))


        _headers = d.pop("headers", UNSET)
        headers: ConfigProviderEncodedHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = ConfigProviderEncodedHeaders.from_dict(_headers)




        _models = d.pop("models", UNSET)
        models: ConfigProviderEncodedModels | Unset
        if isinstance(_models,  Unset):
            models = UNSET
        else:
            models = ConfigProviderEncodedModels.from_dict(_models)




        name = d.pop("name", UNSET)

        package = d.pop("package", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: ConfigProviderSettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = ConfigProviderSettings.from_dict(_settings)




        config_provider_encoded = cls(
            body=body,
            canonical=canonical,
            compatibility=compatibility,
            env=env,
            headers=headers,
            models=models,
            name=name,
            package=package,
            settings=settings,
        )

        return config_provider_encoded

