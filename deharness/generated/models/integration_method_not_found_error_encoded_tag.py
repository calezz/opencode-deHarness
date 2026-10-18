from enum import StrEnum

class IntegrationMethodNotFoundErrorEncodedTag(StrEnum):
    INTEGRATIONMETHODNOTFOUNDERROR = "IntegrationMethodNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
