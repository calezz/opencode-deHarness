from enum import StrEnum

class VoiceWebSocketTransportType(StrEnum):
    WEBSOCKET = "websocket"

    def __str__(self) -> str:
        return str(self.value)
