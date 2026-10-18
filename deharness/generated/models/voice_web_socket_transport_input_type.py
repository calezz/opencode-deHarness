from enum import StrEnum

class VoiceWebSocketTransportInputType(StrEnum):
    WEBSOCKET = "websocket"

    def __str__(self) -> str:
        return str(self.value)
