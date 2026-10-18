from enum import StrEnum

class IntegrationAttemptStatusType0Status(StrEnum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
