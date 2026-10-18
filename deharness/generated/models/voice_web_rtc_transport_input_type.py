from enum import StrEnum

class VoiceWebRTCTransportInputType(StrEnum):
    WEBRTC = "webrtc"

    def __str__(self) -> str:
        return str(self.value)
