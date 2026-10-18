from enum import StrEnum

class SessionMessageCompactionCompletedStatus(StrEnum):
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
