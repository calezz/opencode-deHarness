from enum import StrEnum

class McpLocalConfigEncodedType(StrEnum):
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
