from enum import StrEnum

class SessionInboxSyntheticType(StrEnum):
    SYNTHETIC = "synthetic"

    def __str__(self) -> str:
        return str(self.value)
