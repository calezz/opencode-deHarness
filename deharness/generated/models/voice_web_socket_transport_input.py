from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.voice_web_socket_transport_input_type import VoiceWebSocketTransportInputType






T = TypeVar("T", bound="VoiceWebSocketTransportInput")



@_attrs_define
class VoiceWebSocketTransportInput:
    """ 
        Attributes:
            type_ (VoiceWebSocketTransportInputType):
     """

    type_: VoiceWebSocketTransportInputType





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = VoiceWebSocketTransportInputType(d.pop("type"))




        voice_web_socket_transport_input = cls(
            type_=type_,
        )

        return voice_web_socket_transport_input

