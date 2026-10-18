from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.session_provider_context_version import SessionProviderContextVersion
from typing import cast

if TYPE_CHECKING:
  from ..models.session_provider_context_provenance import SessionProviderContextProvenance





T = TypeVar("T", bound="SessionProviderContext")



@_attrs_define
class SessionProviderContext:
    """ 
        Attributes:
            messages (Any):
            provenance (SessionProviderContextProvenance):
            version (SessionProviderContextVersion):
     """

    messages: Any
    provenance: SessionProviderContextProvenance
    version: SessionProviderContextVersion





    def to_dict(self) -> dict[str, Any]:
        from ..models.session_provider_context_provenance import SessionProviderContextProvenance # noqa: PLC0415
        messages = self.messages

        provenance = self.provenance.to_dict()

        version = self.version.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "messages": messages,
            "provenance": provenance,
            "version": version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_provider_context_provenance import SessionProviderContextProvenance # noqa: PLC0415
        d = dict(src_dict)
        messages = d.pop("messages")

        provenance = SessionProviderContextProvenance.from_dict(d.pop("provenance"))




        version = SessionProviderContextVersion(d.pop("version"))




        session_provider_context = cls(
            messages=messages,
            provenance=provenance,
            version=version,
        )

        return session_provider_context

