from enum import StrEnum

class SessionMessageToolStateCompletedStatus(StrEnum):
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
