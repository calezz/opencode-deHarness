from enum import StrEnum

class IntegrationAttemptStatusType1Status(StrEnum):
    COMPLETE = "complete"

    def __str__(self) -> str:
        return str(self.value)
