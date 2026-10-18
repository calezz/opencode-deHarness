from enum import StrEnum

class ConflictErrorEncodedTag(StrEnum):
    CONFLICTERROR = "ConflictError"

    def __str__(self) -> str:
        return str(self.value)
