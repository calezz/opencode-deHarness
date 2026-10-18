from enum import StrEnum

class WorktreeErrorEncodedTag(StrEnum):
    WORKTREEERROR = "WorktreeError"

    def __str__(self) -> str:
        return str(self.value)
