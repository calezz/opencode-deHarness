from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.model_settings import ModelSettings
  from ..models.model_variant_body import ModelVariantBody
  from ..models.model_variant_headers import ModelVariantHeaders





T = TypeVar("T", bound="ModelVariant")



@_attrs_define
class ModelVariant:
    """ 
        Attributes:
            id (str):
            body (ModelVariantBody | Unset):
            headers (ModelVariantHeaders | Unset):
            settings (ModelSettings | Unset):
     """

    id: str
    body: ModelVariantBody | Unset = UNSET
    headers: ModelVariantHeaders | Unset = UNSET
    settings: ModelSettings | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.model_settings import ModelSettings # noqa: PLC0415
        from ..models.model_variant_body import ModelVariantBody # noqa: PLC0415
        from ..models.model_variant_headers import ModelVariantHeaders # noqa: PLC0415
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
        from ..models.model_settings import ModelSettings # noqa: PLC0415
        from ..models.model_variant_body import ModelVariantBody # noqa: PLC0415
        from ..models.model_variant_headers import ModelVariantHeaders # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        _body = d.pop("body", UNSET)
        body: ModelVariantBody | Unset
        if isinstance(_body,  Unset):
            body = UNSET
        else:
            body = ModelVariantBody.from_dict(_body)




        _headers = d.pop("headers", UNSET)
        headers: ModelVariantHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = ModelVariantHeaders.from_dict(_headers)




        _settings = d.pop("settings", UNSET)
        settings: ModelSettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = ModelSettings.from_dict(_settings)




        model_variant = cls(
            id=id,
            body=body,
            headers=headers,
            settings=settings,
        )

        return model_variant

