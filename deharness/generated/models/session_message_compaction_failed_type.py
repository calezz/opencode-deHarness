from enum import StrEnum

class SessionMessageCompactionFailedType(StrEnum):
    COMPACTION = "compaction"

    def __str__(self) -> str:
        return str(self.value)
