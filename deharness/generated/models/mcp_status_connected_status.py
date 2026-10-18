from enum import StrEnum

class McpStatusConnectedStatus(StrEnum):
    CONNECTED = "connected"

    def __str__(self) -> str:
        return str(self.value)
