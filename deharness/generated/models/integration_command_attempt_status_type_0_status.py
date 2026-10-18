from enum import StrEnum

class IntegrationCommandAttemptStatusType0Status(StrEnum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
