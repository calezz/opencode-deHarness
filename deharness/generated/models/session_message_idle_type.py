from enum import StrEnum

class SessionMessageIdleType(StrEnum):
    IDLE = "idle"

    def __str__(self) -> str:
        return str(self.value)
