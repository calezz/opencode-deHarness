from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.experimental_voice_session_body_session_type_0 import ExperimentalVoiceSessionBodySessionType0
  from ..models.voice_web_rtc_transport_input import VoiceWebRTCTransportInput
  from ..models.voice_web_socket_transport_input import VoiceWebSocketTransportInput





T = TypeVar("T", bound="ExperimentalVoiceSessionBody")



@_attrs_define
class ExperimentalVoiceSessionBody:
    """ 
        Attributes:
            model (str):
            transport (VoiceWebRTCTransportInput | VoiceWebSocketTransportInput):
            session (ExperimentalVoiceSessionBodySessionType0 | None | Unset):
     """

    model: str
    transport: VoiceWebRTCTransportInput | VoiceWebSocketTransportInput
    session: ExperimentalVoiceSessionBodySessionType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.experimental_voice_session_body_session_type_0 import ExperimentalVoiceSessionBodySessionType0 # noqa: PLC0415
        from ..models.voice_web_rtc_transport_input import VoiceWebRTCTransportInput # noqa: PLC0415
        from ..models.voice_web_socket_transport_input import VoiceWebSocketTransportInput # noqa: PLC0415
        model = self.model

        transport: dict[str, Any]
        if isinstance(self.transport, VoiceWebRTCTransportInput):
            transport = self.transport.to_dict()
        else:
            transport = self.transport.to_dict()


        session: dict[str, Any] | None | Unset
        if isinstance(self.session, Unset):
            session = UNSET
        elif isinstance(self.session, ExperimentalVoiceSessionBodySessionType0):
            session = self.session.to_dict()
        else:
            session = self.session


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "model": model,
            "transport": transport,
        })
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.experimental_voice_session_body_session_type_0 import ExperimentalVoiceSessionBodySessionType0 # noqa: PLC0415
        from ..models.voice_web_rtc_transport_input import VoiceWebRTCTransportInput # noqa: PLC0415
        from ..models.voice_web_socket_transport_input import VoiceWebSocketTransportInput # noqa: PLC0415
        d = dict(src_dict)
        model = d.pop("model")

        def _parse_transport(data: object) -> VoiceWebRTCTransportInput | VoiceWebSocketTransportInput:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_voice_transport_input_type_0 = VoiceWebRTCTransportInput.from_dict(data)



                return componentsschemas_voice_transport_input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_voice_transport_input_type_1 = VoiceWebSocketTransportInput.from_dict(data)



            return componentsschemas_voice_transport_input_type_1

        transport = _parse_transport(d.pop("transport"))


        def _parse_session(data: object) -> ExperimentalVoiceSessionBodySessionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_type_0 = ExperimentalVoiceSessionBodySessionType0.from_dict(data)



                return session_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExperimentalVoiceSessionBodySessionType0 | None | Unset, data)

        session = _parse_session(d.pop("session", UNSET))


        experimental_voice_session_body = cls(
            model=model,
            transport=transport,
            session=session,
        )

        return experimental_voice_session_body

