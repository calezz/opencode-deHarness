from enum import StrEnum

class IntegrationAttemptStatusType2Status(StrEnum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
