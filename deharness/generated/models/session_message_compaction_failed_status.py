from enum import StrEnum

class SessionMessageCompactionFailedStatus(StrEnum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
