from enum import StrEnum

class CommandNotFoundErrorEncodedTag(StrEnum):
    COMMANDNOTFOUNDERROR = "CommandNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
