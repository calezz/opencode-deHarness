from enum import StrEnum

class PluginStateType1Status(StrEnum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
