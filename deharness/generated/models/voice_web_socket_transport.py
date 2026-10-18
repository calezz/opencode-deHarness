from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.voice_web_socket_transport_expires_at_type_1 import VoiceWebSocketTransportExpiresAtType1
from ..models.voice_web_socket_transport_type import VoiceWebSocketTransportType
from typing import cast






T = TypeVar("T", bound="VoiceWebSocketTransport")



@_attrs_define
class VoiceWebSocketTransport:
    """ 
        Attributes:
            expires_at (float | VoiceWebSocketTransportExpiresAtType1):
            token (str):
            type_ (VoiceWebSocketTransportType):
            url (str):
     """

    expires_at: float | VoiceWebSocketTransportExpiresAtType1
    token: str
    type_: VoiceWebSocketTransportType
    url: str





    def to_dict(self) -> dict[str, Any]:
        expires_at: float | str
        if isinstance(self.expires_at, VoiceWebSocketTransportExpiresAtType1):
            expires_at = self.expires_at.value
        else:
            expires_at = self.expires_at

        token = self.token

        type_ = self.type_.value

        url = self.url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "expiresAt": expires_at,
            "token": token,
            "type": type_,
            "url": url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_expires_at(data: object) -> float | VoiceWebSocketTransportExpiresAtType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_1 = VoiceWebSocketTransportExpiresAtType1(data)



                return expires_at_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | VoiceWebSocketTransportExpiresAtType1, data)

        expires_at = _parse_expires_at(d.pop("expiresAt"))


        token = d.pop("token")

        type_ = VoiceWebSocketTransportType(d.pop("type"))




        url = d.pop("url")

        voice_web_socket_transport = cls(
            expires_at=expires_at,
            token=token,
            type_=type_,
            url=url,
        )

        return voice_web_socket_transport

