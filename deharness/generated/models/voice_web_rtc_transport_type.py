from enum import StrEnum

class VoiceWebRTCTransportType(StrEnum):
    WEBRTC = "webrtc"

    def __str__(self) -> str:
        return str(self.value)
