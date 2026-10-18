from enum import StrEnum

class SessionMessageCompactionRunningStatus(StrEnum):
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
