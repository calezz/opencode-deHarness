from enum import StrEnum

class IntegrationCommandAttemptStatusType1Status(StrEnum):
    COMPLETE = "complete"

    def __str__(self) -> str:
        return str(self.value)
