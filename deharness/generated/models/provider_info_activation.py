from enum import StrEnum

class ProviderInfoActivation(StrEnum):
    AUTO = "auto"
    DISABLED = "disabled"
    ENABLED = "enabled"

    def __str__(self) -> str:
        return str(self.value)
