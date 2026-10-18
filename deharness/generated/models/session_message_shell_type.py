from enum import StrEnum

class SessionMessageShellType(StrEnum):
    SHELL = "shell"

    def __str__(self) -> str:
        return str(self.value)
