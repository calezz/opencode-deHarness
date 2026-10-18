from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.config_model_encoded_variants_item_body import ConfigModelEncodedVariantsItemBody
  from ..models.config_model_encoded_variants_item_headers import ConfigModelEncodedVariantsItemHeaders
  from ..models.config_model_settings import ConfigModelSettings





T = TypeVar("T", bound="ConfigModelEncodedVariantsItem")



@_attrs_define
class ConfigModelEncodedVariantsItem:
    """ 
        Attributes:
            id (str):
            body (ConfigModelEncodedVariantsItemBody | Unset):
            headers (ConfigModelEncodedVariantsItemHeaders | Unset):
            settings (ConfigModelSettings | Unset):
     """

    id: str
    body: ConfigModelEncodedVariantsItemBody | Unset = UNSET
    headers: ConfigModelEncodedVariantsItemHeaders | Unset = UNSET
    settings: ConfigModelSettings | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.config_model_encoded_variants_item_body import ConfigModelEncodedVariantsItemBody # noqa: PLC0415
        from ..models.config_model_encoded_variants_item_headers import ConfigModelEncodedVariantsItemHeaders # noqa: PLC0415
        from ..models.config_model_settings import ConfigModelSettings # noqa: PLC0415
        id = self.id

        body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
        })
        if body is not UNSET:
            field_dict["body"] = body
        if headers is not UNSET:
            field_dict["headers"] = headers
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_model_encoded_variants_item_body import ConfigModelEncodedVariantsItemBody # noqa: PLC0415
        from ..models.config_model_encoded_variants_item_headers import ConfigModelEncodedVariantsItemHeaders # noqa: PLC0415
        from ..models.config_model_settings import ConfigModelSettings # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        _body = d.pop("body", UNSET)
        body: ConfigModelEncodedVariantsItemBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = ConfigModelEncodedVariantsItemBody.from_dict(_body)




        _headers = d.pop("headers", UNSET)
        headers: ConfigModelEncodedVariantsItemHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = ConfigModelEncodedVariantsItemHeaders.from_dict(_headers)




        _settings = d.pop("settings", UNSET)
        settings: ConfigModelSettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = ConfigModelSettings.from_dict(_settings)




        config_model_encoded_variants_item = cls(
            id=id,
            body=body,
            headers=headers,
            settings=settings,
        )

        return config_model_encoded_variants_item

