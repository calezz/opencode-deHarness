from enum import StrEnum

class WorktreeErrorEncodedName(StrEnum):
    WORKTREEERROR = "WorktreeError"

    def __str__(self) -> str:
        return str(self.value)
