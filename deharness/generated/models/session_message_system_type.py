from enum import StrEnum

class SessionMessageSystemType(StrEnum):
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
