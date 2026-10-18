from enum import StrEnum

class ServiceUnavailableErrorEncodedTag(StrEnum):
    SERVICEUNAVAILABLEERROR = "ServiceUnavailableError"

    def __str__(self) -> str:
        return str(self.value)
