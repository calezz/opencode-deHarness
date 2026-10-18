from enum import StrEnum

class SessionNotFoundErrorEncodedTag(StrEnum):
    SESSIONNOTFOUNDERROR = "SessionNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
