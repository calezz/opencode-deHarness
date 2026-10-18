from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.model_info_status import ModelInfoStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.model_capabilities import ModelCapabilities
  from ..models.model_compatibility import ModelCompatibility
  from ..models.model_cost import ModelCost
  from ..models.model_info_body import ModelInfoBody
  from ..models.model_info_headers import ModelInfoHeaders
  from ..models.model_info_limit import ModelInfoLimit
  from ..models.model_info_time import ModelInfoTime
  from ..models.model_settings import ModelSettings
  from ..models.model_variant import ModelVariant





T = TypeVar("T", bound="ModelInfo")



@_attrs_define
class ModelInfo:
    """ 
        Attributes:
            capabilities (ModelCapabilities):
            cost (list[ModelCost]):
            enabled (bool):
            id (str):
            limit (ModelInfoLimit):
            model_id (str):
            name (str):
            provider_id (str):
            status (ModelInfoStatus):
            time (ModelInfoTime):
            variants (list[ModelVariant]):
            body (ModelInfoBody | Unset):
            canonical (str | Unset):
            compatibility (ModelCompatibility | Unset):
            family (str | Unset):
            headers (ModelInfoHeaders | Unset):
            package (str | Unset):
            settings (ModelSettings | Unset):
     """

    capabilities: ModelCapabilities
    cost: list[ModelCost]
    enabled: bool
    id: str
    limit: ModelInfoLimit
    model_id: str
    name: str
    provider_id: str
    status: ModelInfoStatus
    time: ModelInfoTime
    variants: list[ModelVariant]
    body: ModelInfoBody | Unset = UNSET
    canonical: str | Unset = UNSET
    compatibility: ModelCompatibility | Unset = UNSET
    family: str | Unset = UNSET
    headers: ModelInfoHeaders | Unset = UNSET
    package: str | Unset = UNSET
    settings: ModelSettings | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_capabilities import ModelCapabilities # noqa: PLC0415
        from ..models.model_compatibility import ModelCompatibility # noqa: PLC0415
        from ..models.model_cost import ModelCost # noqa: PLC0415
        from ..models.model_info_body import ModelInfoBody # noqa: PLC0415
        from ..models.model_info_headers import ModelInfoHeaders # noqa: PLC0415
        from ..models.model_info_limit import ModelInfoLimit # noqa: PLC0415
        from ..models.model_info_time import ModelInfoTime # noqa: PLC0415
        from ..models.model_settings import ModelSettings # noqa: PLC0415
        from ..models.model_variant import ModelVariant # noqa: PLC0415
        capabilities = self.capabilities.to_dict()

        cost = []
        for cost_item_data in self.cost:
            cost_item = cost_item_data.to_dict()
            cost.append(cost_item)



        enabled = self.enabled

        id = self.id

        limit = self.limit.to_dict()

        model_id = self.model_id

        name = self.name

        provider_id = self.provider_id

        status = self.status.value

        time = self.time.to_dict()

        variants = []
        for variants_item_data in self.variants:
            variants_item = variants_item_data.to_dict()
            variants.append(variants_item)



        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        canonical = self.canonical

        compatibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compatibility, Unset):
            compatibility = self.compatibility.to_dict()

        family = self.family

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        package = self.package

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "capabilities": capabilities,
            "cost": cost,
            "enabled": enabled,
            "id": id,
            "limit": limit,
            "modelID": model_id,
            "name": name,
            "providerID": provider_id,
            "status": status,
            "time": time,
            "variants": variants,
        })
        if body is not UNSET:
            field_dict["body"] = body
        if canonical is not UNSET:
            field_dict["canonical"] = canonical
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility
        if family is not UNSET:
            field_dict["family"] = family
        if headers is not UNSET:
            field_dict["headers"] = headers
        if package is not UNSET:
            field_dict["package"] = package
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_capabilities import ModelCapabilities # noqa: PLC0415
        from ..models.model_compatibility import ModelCompatibility # noqa: PLC0415
        from ..models.model_cost import ModelCost # noqa: PLC0415
        from ..models.model_info_body import ModelInfoBody # noqa: PLC0415
        from ..models.model_info_headers import ModelInfoHeaders # noqa: PLC0415
        from ..models.model_info_limit import ModelInfoLimit # noqa: PLC0415
        from ..models.model_info_time import ModelInfoTime # noqa: PLC0415
        from ..models.model_settings import ModelSettings # noqa: PLC0415
        from ..models.model_variant import ModelVariant # noqa: PLC0415
        d = dict(src_dict)
        capabilities = ModelCapabilities.from_dict(d.pop("capabilities"))




        cost = []
        _cost = d.pop("cost")
        for cost_item_data in (_cost):
            cost_item = ModelCost.from_dict(cost_item_data)



            cost.append(cost_item)


        enabled = d.pop("enabled")

        id = d.pop("id")

        limit = ModelInfoLimit.from_dict(d.pop("limit"))




        model_id = d.pop("modelID")

        name = d.pop("name")

        provider_id = d.pop("providerID")

        status = ModelInfoStatus(d.pop("status"))




        time = ModelInfoTime.from_dict(d.pop("time"))




        variants = []
        _variants = d.pop("variants")
        for variants_item_data in (_variants):
            variants_item = ModelVariant.from_dict(variants_item_data)



            variants.append(variants_item)


        _body = d.pop("body", UNSET)
        body: ModelInfoBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = ModelInfoBody.from_dict(_body)




        canonical = d.pop("canonical", UNSET)

        _compatibility = d.pop("compatibility", UNSET)
        compatibility: ModelCompatibility | Unset
        if isinstance(_compatibility,  Unset):
            compatibility = UNSET
        else:
            compatibility = ModelCompatibility.from_dict(_compatibility)




        family = d.pop("family", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: ModelInfoHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = ModelInfoHeaders.from_dict(_headers)




        package = d.pop("package", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: ModelSettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = ModelSettings.from_dict(_settings)




        model_info = cls(
            capabilities=capabilities,
            cost=cost,
            enabled=enabled,
            id=id,
            limit=limit,
            model_id=model_id,
            name=name,
            provider_id=provider_id,
            status=status,
            time=time,
            variants=variants,
            body=body,
            canonical=canonical,
            compatibility=compatibility,
            family=family,
            headers=headers,
            package=package,
            settings=settings,
        )

        return model_info

