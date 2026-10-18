from enum import StrEnum

class PluginSourceType3Type(StrEnum):
    SDK = "sdk"

    def __str__(self) -> str:
        return str(self.value)
