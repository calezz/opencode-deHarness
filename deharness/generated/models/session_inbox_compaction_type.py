from enum import StrEnum

class SessionInboxCompactionType(StrEnum):
    COMPACTION = "compaction"

    def __str__(self) -> str:
        return str(self.value)
