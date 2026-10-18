from enum import StrEnum

class ConfigInfoEncodedUpdate(StrEnum):
    AUTO = "auto"
    DISABLE = "disable"
    NOTIFY = "notify"

    def __str__(self) -> str:
        return str(self.value)
