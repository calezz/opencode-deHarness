from enum import StrEnum

class McpStatusDisabledStatus(StrEnum):
    DISABLED = "disabled"

    def __str__(self) -> str:
        return str(self.value)
