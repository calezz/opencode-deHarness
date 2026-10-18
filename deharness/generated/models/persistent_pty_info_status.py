from enum import StrEnum

class PersistentPtyInfoStatus(StrEnum):
    EXITED = "exited"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
