from enum import StrEnum

class SessionForkBoundaryType0Type(StrEnum):
    BEFORE = "before"

    def __str__(self) -> str:
        return str(self.value)
