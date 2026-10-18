from enum import StrEnum

class PtyStatus(StrEnum):
    EXITED = "exited"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
