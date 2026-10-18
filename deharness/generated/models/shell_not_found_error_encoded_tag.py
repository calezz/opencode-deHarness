from enum import StrEnum

class ShellNotFoundErrorEncodedTag(StrEnum):
    SHELLNOTFOUNDERROR = "ShellNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
