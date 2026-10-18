from enum import StrEnum

class CommandExecutionErrorEncodedTag(StrEnum):
    COMMANDEXECUTIONERROR = "CommandExecutionError"

    def __str__(self) -> str:
        return str(self.value)
