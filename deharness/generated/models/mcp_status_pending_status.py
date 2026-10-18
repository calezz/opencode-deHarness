from enum import StrEnum

class McpStatusPendingStatus(StrEnum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
