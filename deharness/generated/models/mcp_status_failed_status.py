from enum import StrEnum

class McpStatusFailedStatus(StrEnum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
