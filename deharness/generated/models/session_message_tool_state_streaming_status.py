from enum import StrEnum

class SessionMessageToolStateStreamingStatus(StrEnum):
    STREAMING = "streaming"

    def __str__(self) -> str:
        return str(self.value)
