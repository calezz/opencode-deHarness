from enum import StrEnum

class IntegrationAttemptNotFoundErrorEncodedTag(StrEnum):
    INTEGRATIONATTEMPTNOTFOUNDERROR = "IntegrationAttemptNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
