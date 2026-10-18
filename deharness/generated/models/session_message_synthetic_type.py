from enum import StrEnum

class SessionMessageSyntheticType(StrEnum):
    SYNTHETIC = "synthetic"

    def __str__(self) -> str:
        return str(self.value)
