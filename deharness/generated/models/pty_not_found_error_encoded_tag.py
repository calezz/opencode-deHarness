from enum import StrEnum

class PtyNotFoundErrorEncodedTag(StrEnum):
    PTYNOTFOUNDERROR = "PtyNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
