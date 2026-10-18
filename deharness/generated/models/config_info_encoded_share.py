from enum import StrEnum

class ConfigInfoEncodedShare(StrEnum):
    AUTO = "auto"
    DISABLED = "disabled"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
