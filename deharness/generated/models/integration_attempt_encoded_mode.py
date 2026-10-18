from enum import StrEnum

class IntegrationAttemptEncodedMode(StrEnum):
    AUTO = "auto"
    CODE = "code"

    def __str__(self) -> str:
        return str(self.value)
