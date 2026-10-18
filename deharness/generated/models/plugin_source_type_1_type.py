from enum import StrEnum

class PluginSourceType1Type(StrEnum):
    PACKAGE = "package"

    def __str__(self) -> str:
        return str(self.value)
