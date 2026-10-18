from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.voice_web_rtc_transport_input_dcid_type_0_type_1 import VoiceWebRTCTransportInputDcidType0Type1
from ..models.voice_web_rtc_transport_input_type import VoiceWebRTCTransportInputType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="VoiceWebRTCTransportInput")



@_attrs_define
class VoiceWebRTCTransportInput:
    """ 
        Attributes:
            sdp (str):
            type_ (VoiceWebRTCTransportInputType):
            dcid (float | None | Unset | VoiceWebRTCTransportInputDcidType0Type1):
     """

    sdp: str
    type_: VoiceWebRTCTransportInputType
    dcid: float | None | Unset | VoiceWebRTCTransportInputDcidType0Type1 = UNSET





    def to_dict(self) -> dict[str, Any]:
        sdp = self.sdp

        type_ = self.type_.value

        dcid: float | None | str | Unset
        if isinstance(self.dcid, Unset):
            dcid = UNSET
        elif isinstance(self.dcid, VoiceWebRTCTransportInputDcidType0Type1):
            dcid = self.dcid.value
        else:
            dcid = self.dcid


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "sdp": sdp,
            "type": type_,
        })
        if dcid is not UNSET:
            field_dict["dcid"] = dcid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sdp = d.pop("sdp")

        type_ = VoiceWebRTCTransportInputType(d.pop("type"))




        def _parse_dcid(data: object) -> float | None | Unset | VoiceWebRTCTransportInputDcidType0Type1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dcid_type_0_type_1 = VoiceWebRTCTransportInputDcidType0Type1(data)



                return dcid_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | None | Unset | VoiceWebRTCTransportInputDcidType0Type1, data)

        dcid = _parse_dcid(d.pop("dcid", UNSET))


        voice_web_rtc_transport_input = cls(
            sdp=sdp,
            type_=type_,
            dcid=dcid,
        )

        return voice_web_rtc_transport_input

