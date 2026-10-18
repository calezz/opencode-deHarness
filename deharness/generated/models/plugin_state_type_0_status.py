from enum import StrEnum

class PluginStateType0Status(StrEnum):
    ACTIVE = "active"

    def __str__(self) -> str:
        return str(self.value)
