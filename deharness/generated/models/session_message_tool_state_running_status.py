from enum import StrEnum

class SessionMessageToolStateRunningStatus(StrEnum):
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
