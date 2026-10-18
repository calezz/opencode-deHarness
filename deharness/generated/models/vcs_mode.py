from enum import StrEnum

class VcsMode(StrEnum):
    BRANCH = "branch"
    COMMITTED = "committed"
    WORKING = "working"

    def __str__(self) -> str:
        return str(self.value)
