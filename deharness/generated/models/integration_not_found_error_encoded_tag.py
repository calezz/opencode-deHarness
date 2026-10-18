from enum import StrEnum

class IntegrationNotFoundErrorEncodedTag(StrEnum):
    INTEGRATIONNOTFOUNDERROR = "IntegrationNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
