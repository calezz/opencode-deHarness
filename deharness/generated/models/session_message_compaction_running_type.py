from enum import StrEnum

class SessionMessageCompactionRunningType(StrEnum):
    COMPACTION = "compaction"

    def __str__(self) -> str:
        return str(self.value)
