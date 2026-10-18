from enum import StrEnum

class ProviderTransport(StrEnum):
    HTTP = "http"
    WEBSOCKET = "websocket"

    def __str__(self) -> str:
        return str(self.value)
