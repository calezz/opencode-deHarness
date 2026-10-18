from enum import StrEnum

class PluginSourceType0Type(StrEnum):
    BUILTIN = "builtin"

    def __str__(self) -> str:
        return str(self.value)
