from enum import StrEnum

class McpServerNotFoundErrorEncodedTag(StrEnum):
    MCPSERVERNOTFOUNDERROR = "McpServerNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
