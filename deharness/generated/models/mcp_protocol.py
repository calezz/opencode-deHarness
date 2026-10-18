from enum import StrEnum

class McpProtocol(StrEnum):
    AUTO = "auto"
    LEGACY = "legacy"
    VALUE_2 = "2026-07-28"

    def __str__(self) -> str:
        return str(self.value)
