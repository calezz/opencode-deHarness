from enum import StrEnum

class IntegrationAttemptStatusType3Status(StrEnum):
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
