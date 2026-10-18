from enum import StrEnum

class VoiceWebRTCTransportInputDcidType0Type1(StrEnum):
    INFINITY = "Infinity"
    NAN = "NaN"
    VALUE_1 = "-Infinity"

    def __str__(self) -> str:
        return str(self.value)
