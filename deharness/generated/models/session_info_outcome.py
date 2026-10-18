from enum import StrEnum

class SessionInfoOutcome(StrEnum):
    FAILED = "failed"
    INTERRUPTED = "interrupted"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
