from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.voice_web_rtc_transport_type import VoiceWebRTCTransportType






T = TypeVar("T", bound="VoiceWebRTCTransport")



@_attrs_define
class VoiceWebRTCTransport:
    """ 
        Attributes:
            sdp (str):
            type_ (VoiceWebRTCTransportType):
     """

    sdp: str
    type_: VoiceWebRTCTransportType





    def to_dict(self) -> dict[str, Any]:
        sdp = self.sdp

        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "sdp": sdp,
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sdp = d.pop("sdp")

        type_ = VoiceWebRTCTransportType(d.pop("type"))




        voice_web_rtc_transport = cls(
            sdp=sdp,
            type_=type_,
        )

        return voice_web_rtc_transport

