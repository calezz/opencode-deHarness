from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.provider_info_activation import ProviderInfoActivation
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.provider_compatibility import ProviderCompatibility
  from ..models.provider_info_body import ProviderInfoBody
  from ..models.provider_info_headers import ProviderInfoHeaders
  from ..models.provider_settings import ProviderSettings





T = TypeVar("T", bound="ProviderInfo")



@_attrs_define
class ProviderInfo:
    """ 
        Attributes:
            activation (ProviderInfoActivation):
            id (str):
            name (str):
            package (str):
            body (ProviderInfoBody | Unset):
            canonical (str | Unset):
            compatibility (ProviderCompatibility | Unset):
            headers (ProviderInfoHeaders | Unset):
            integration_id (str | Unset):
            settings (ProviderSettings | Unset):
     """

    activation: ProviderInfoActivation
    id: str
    name: str
    package: str
    body: ProviderInfoBody | Unset = UNSET
    canonical: str | Unset = UNSET
    compatibility: ProviderCompatibility | Unset = UNSET
    headers: ProviderInfoHeaders | Unset = UNSET
    integration_id: str | Unset = UNSET
    settings: ProviderSettings | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_compatibility import ProviderCompatibility # noqa: PLC0415
        from ..models.provider_info_body import ProviderInfoBody # noqa: PLC0415
        from ..models.provider_info_headers import ProviderInfoHeaders # noqa: PLC0415
        from ..models.provider_settings import ProviderSettings # noqa: PLC0415
        activation = self.activation.value

        id = self.id

        name = self.name

        package = self.package

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        canonical = self.canonical

        compatibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compatibility, Unset):
            compatibility = self.compatibility.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        integration_id = self.integration_id

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "activation": activation,
            "id": id,
            "name": name,
            "package": package,
        })
        if body is not UNSET:
            field_dict["body"] = body
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility
        if headers is not UNSET:
            field_dict["headers"] = headers
        if integration_id is not UNSET:
            field_dict["integrationID"] = integration_id
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_compatibility import ProviderCompatibility # noqa: PLC0415
        from ..models.provider_info_body import ProviderInfoBody # noqa: PLC0415
        from ..models.provider_info_headers import ProviderInfoHeaders # noqa: PLC0415
        from ..models.provider_settings import ProviderSettings # noqa: PLC0415
        d = dict(src_dict)
        activation = ProviderInfoActivation(d.pop("activation"))




        id = d.pop("id")

        name = d.pop("name")

        package = d.pop("package")

        _body = d.pop("body", UNSET)
        body: ProviderInfoBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = ProviderInfoBody.from_dict(_body)




        canonical = d.pop("canonical", UNSET)

        _compatibility = d.pop("compatibility", UNSET)
        compatibility: ProviderCompatibility | Unset
        if isinstance(_compatibility,  Unset):
            compatibility = UNSET
        else:
            compatibility = ProviderCompatibility.from_dict(_compatibility)




        _headers = d.pop("headers", UNSET)
        headers: ProviderInfoHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = ProviderInfoHeaders.from_dict(_headers)




        integration_id = d.pop("integrationID", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: ProviderSettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = ProviderSettings.from_dict(_settings)




        provider_info = cls(
            activation=activation,
            id=id,
            name=name,
            package=package,
            body=body,
            canonical=canonical,
            compatibility=compatibility,
            headers=headers,
            integration_id=integration_id,
            settings=settings,
        )

        return provider_info

