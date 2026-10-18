from enum import StrEnum

class PluginSourceType2Type(StrEnum):
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
