from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.voice_web_rtc_transport import VoiceWebRTCTransport
  from ..models.voice_web_socket_transport import VoiceWebSocketTransport





T = TypeVar("T", bound="VoiceSessionResponseData")



@_attrs_define
class VoiceSessionResponseData:
    """ 
        Attributes:
            transport (VoiceWebRTCTransport | VoiceWebSocketTransport):
     """

    transport: VoiceWebRTCTransport | VoiceWebSocketTransport





    def to_dict(self) -> dict[str, Any]:
        from ..models.voice_web_rtc_transport import VoiceWebRTCTransport # noqa: PLC0415
        from ..models.voice_web_socket_transport import VoiceWebSocketTransport # noqa: PLC0415
        transport: dict[str, Any]
        if isinstance(self.transport, VoiceWebRTCTransport):
            transport = self.transport.to_dict()
        else:
            transport = self.transport.to_dict()



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "transport": transport,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.voice_web_rtc_transport import VoiceWebRTCTransport # noqa: PLC0415
        from ..models.voice_web_socket_transport import VoiceWebSocketTransport # noqa: PLC0415
        d = dict(src_dict)
        def _parse_transport(data: object) -> VoiceWebRTCTransport | VoiceWebSocketTransport:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_voice_transport_type_0 = VoiceWebRTCTransport.from_dict(data)



                return componentsschemas_voice_transport_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_voice_transport_type_1 = VoiceWebSocketTransport.from_dict(data)



            return componentsschemas_voice_transport_type_1

        transport = _parse_transport(d.pop("transport"))


        voice_session_response_data = cls(
            transport=transport,
        )

        return voice_session_response_data

