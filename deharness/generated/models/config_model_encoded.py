from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_model_capabilities import ConfigModelCapabilities
  from ..models.config_model_cost_encoded import ConfigModelCostEncoded
  from ..models.config_model_encoded_body import ConfigModelEncodedBody
  from ..models.config_model_encoded_headers import ConfigModelEncodedHeaders
  from ..models.config_model_encoded_limit import ConfigModelEncodedLimit
  from ..models.config_model_encoded_variants_item import ConfigModelEncodedVariantsItem
  from ..models.config_model_settings import ConfigModelSettings
  from ..models.model_compatibility import ModelCompatibility





T = TypeVar("T", bound="ConfigModelEncoded")



@_attrs_define
class ConfigModelEncoded:
    """ 
        Attributes:
            body (ConfigModelEncodedBody | Unset):
            capabilities (ConfigModelCapabilities | Unset):
            compatibility (ModelCompatibility | Unset):
            cost (ConfigModelCostEncoded | list[ConfigModelCostEncoded] | Unset):
            disabled (bool | Unset):
            family (str | Unset):
            headers (ConfigModelEncodedHeaders | Unset):
            limit (ConfigModelEncodedLimit | Unset):
            model_id (str | Unset):
            name (str | Unset):
            package (str | Unset):
            release_date (str | Unset): Release date as YYYY-MM-DD or YYYY-MM
            settings (ConfigModelSettings | Unset):
            variants (list[ConfigModelEncodedVariantsItem] | Unset):
     """

    body: ConfigModelEncodedBody | Unset = UNSET
    capabilities: ConfigModelCapabilities | Unset = UNSET
    compatibility: ModelCompatibility | Unset = UNSET
    cost: ConfigModelCostEncoded | list[ConfigModelCostEncoded] | Unset = UNSET
    disabled: bool | Unset = UNSET
    family: str | Unset = UNSET
    headers: ConfigModelEncodedHeaders | Unset = UNSET
    limit: ConfigModelEncodedLimit | Unset = UNSET
    model_id: str | Unset = UNSET
    name: str | Unset = UNSET
    package: str | Unset = UNSET
    release_date: str | Unset = UNSET
    settings: ConfigModelSettings | Unset = UNSET
    variants: list[ConfigModelEncodedVariantsItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_model_capabilities import ConfigModelCapabilities # noqa: PLC0415
        from ..models.config_model_cost_encoded import ConfigModelCostEncoded # noqa: PLC0415
        from ..models.config_model_encoded_body import ConfigModelEncodedBody # noqa: PLC0415
        from ..models.config_model_encoded_headers import ConfigModelEncodedHeaders # noqa: PLC0415
        from ..models.config_model_encoded_limit import ConfigModelEncodedLimit # noqa: PLC0415
        from ..models.config_model_encoded_variants_item import ConfigModelEncodedVariantsItem # noqa: PLC0415
        from ..models.config_model_settings import ConfigModelSettings # noqa: PLC0415
        from ..models.model_compatibility import ModelCompatibility # noqa: PLC0415
        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        capabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        compatibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compatibility, Unset):
            compatibility = self.compatibility.to_dict()

        cost: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.cost, Unset):
            cost = UNSET
        elif isinstance(self.cost, ConfigModelCostEncoded):
            cost = self.cost.to_dict()
        else:
            cost = []
            for cost_type_1_item_data in self.cost:
                cost_type_1_item = cost_type_1_item_data.to_dict()
                cost.append(cost_type_1_item)




        disabled = self.disabled

        family = self.family

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limit, Unset):
            limit = self.limit.to_dict()

        model_id = self.model_id

        name = self.name

        package = self.package

        release_date = self.release_date

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        variants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variants, Unset):
            variants = []
            for variants_item_data in self.variants:
                variants_item = variants_item_data.to_dict()
                variants.append(variants_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if body is not UNSET:
            field_dict["body"] = body
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if compatibility is not UNSET:
            field_dict["compatibility"] = compatibility
        if cost is not UNSET:
            field_dict["cost"] = cost
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if family is not UNSET:
            field_dict["family"] = family
        if headers is not UNSET:
            field_dict["headers"] = headers
        if limit is not UNSET:
            field_dict["limit"] = limit
        if model_id is not UNSET:
            field_dict["modelID"] = model_id
        if name is not UNSET:
            field_dict["name"] = name
        if package is not UNSET:
            field_dict["package"] = package
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if settings is not UNSET:
            field_dict["settings"] = settings
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_model_capabilities import ConfigModelCapabilities # noqa: PLC0415
        from ..models.config_model_cost_encoded import ConfigModelCostEncoded # noqa: PLC0415
        from ..models.config_model_encoded_body import ConfigModelEncodedBody # noqa: PLC0415
        from ..models.config_model_encoded_headers import ConfigModelEncodedHeaders # noqa: PLC0415
        from ..models.config_model_encoded_limit import ConfigModelEncodedLimit # noqa: PLC0415
        from ..models.config_model_encoded_variants_item import ConfigModelEncodedVariantsItem # noqa: PLC0415
        from ..models.config_model_settings import ConfigModelSettings # noqa: PLC0415
        from ..models.model_compatibility import ModelCompatibility # noqa: PLC0415
        d = dict(src_dict)
        _body = d.pop("body", UNSET)
        body: ConfigModelEncodedBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = ConfigModelEncodedBody.from_dict(_body)




        _capabilities = d.pop("capabilities", UNSET)
        capabilities: ConfigModelCapabilities | Unset
        if isinstance(_capabilities,  Unset):
            capabilities = UNSET
        else:
            capabilities = ConfigModelCapabilities.from_dict(_capabilities)




        _compatibility = d.pop("compatibility", UNSET)
        compatibility: ModelCompatibility | Unset
        if isinstance(_compatibility,  Unset):
            compatibility = UNSET
        else:
            compatibility = ModelCompatibility.from_dict(_compatibility)




        def _parse_cost(data: object) -> ConfigModelCostEncoded | list[ConfigModelCostEncoded] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cost_type_0 = ConfigModelCostEncoded.from_dict(data)



                return cost_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            cost_type_1 = []
            _cost_type_1 = data
            for cost_type_1_item_data in (_cost_type_1):
                cost_type_1_item = ConfigModelCostEncoded.from_dict(cost_type_1_item_data)



                cost_type_1.append(cost_type_1_item)

            return cost_type_1

        cost = _parse_cost(d.pop("cost", UNSET))


        disabled = d.pop("disabled", UNSET)

        family = d.pop("family", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: ConfigModelEncodedHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = ConfigModelEncodedHeaders.from_dict(_headers)




        _limit = d.pop("limit", UNSET)
        limit: ConfigModelEncodedLimit | Unset
        if isinstance(_limit,  Unset):
            limit = UNSET
        else:
            limit = ConfigModelEncodedLimit.from_dict(_limit)




        model_id = d.pop("modelID", UNSET)

        name = d.pop("name", UNSET)

        package = d.pop("package", UNSET)

        release_date = d.pop("releaseDate", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: ConfigModelSettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = ConfigModelSettings.from_dict(_settings)




        _variants = d.pop("variants", UNSET)
        variants: list[ConfigModelEncodedVariantsItem] | Unset = UNSET
        if _variants is not UNSET:
            variants = []
            for variants_item_data in _variants:
                variants_item = ConfigModelEncodedVariantsItem.from_dict(variants_item_data)



                variants.append(variants_item)


        config_model_encoded = cls(
            body=body,
            capabilities=capabilities,
            compatibility=compatibility,
            cost=cost,
            disabled=disabled,
            family=family,
            headers=headers,
            limit=limit,
            model_id=model_id,
            name=name,
            package=package,
            release_date=release_date,
            settings=settings,
            variants=variants,
        )

        return config_model_encoded

