from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SessionProviderContextProvenance")



@_attrs_define
class SessionProviderContextProvenance:
    """ 
        Attributes:
            endpoint (str):
            model_id (str):
            protocol (str):
            provider (str):
            provider_id (str):
            route (str):
     """

    endpoint: str
    model_id: str
    protocol: str
    provider: str
    provider_id: str
    route: str





    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        model_id = self.model_id

        protocol = self.protocol

        provider = self.provider

        provider_id = self.provider_id

        route = self.route


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "endpoint": endpoint,
            "modelID": model_id,
            "protocol": protocol,
            "provider": provider,
            "providerID": provider_id,
            "route": route,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        model_id = d.pop("modelID")

        protocol = d.pop("protocol")

        provider = d.pop("provider")

        provider_id = d.pop("providerID")

        route = d.pop("route")

        session_provider_context_provenance = cls(
            endpoint=endpoint,
            model_id=model_id,
            protocol=protocol,
            provider=provider,
            provider_id=provider_id,
            route=route,
        )

        return session_provider_context_provenance

