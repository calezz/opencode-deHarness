from enum import StrEnum

class SessionMessageCompactionCompletedType(StrEnum):
    COMPACTION = "compaction"

    def __str__(self) -> str:
        return str(self.value)
