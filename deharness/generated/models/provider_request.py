from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.provider_request_body import ProviderRequestBody
  from ..models.provider_request_headers import ProviderRequestHeaders
  from ..models.provider_settings import ProviderSettings





T = TypeVar("T", bound="ProviderRequest")



@_attrs_define
class ProviderRequest:
    """ 
        Attributes:
            body (ProviderRequestBody):
            headers (ProviderRequestHeaders):
            settings (ProviderSettings):
     """

    body: ProviderRequestBody
    headers: ProviderRequestHeaders
    settings: ProviderSettings





    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_request_body import ProviderRequestBody # noqa: PLC0415
        from ..models.provider_request_headers import ProviderRequestHeaders # noqa: PLC0415
        from ..models.provider_settings import ProviderSettings # noqa: PLC0415
        body = self.body.to_dict()

        headers = self.headers.to_dict()

        settings = self.settings.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "body": body,
            "headers": headers,
            "settings": settings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_request_body import ProviderRequestBody # noqa: PLC0415
        from ..models.provider_request_headers import ProviderRequestHeaders # noqa: PLC0415
        from ..models.provider_settings import ProviderSettings # noqa: PLC0415
        d = dict(src_dict)
        body = ProviderRequestBody.from_dict(d.pop("body"))




        headers = ProviderRequestHeaders.from_dict(d.pop("headers"))




        settings = ProviderSettings.from_dict(d.pop("settings"))




        provider_request = cls(
            body=body,
            headers=headers,
            settings=settings,
        )

        return provider_request

