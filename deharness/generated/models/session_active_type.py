from enum import StrEnum

class SessionActiveType(StrEnum):
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
