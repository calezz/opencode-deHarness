from enum import StrEnum

class ReferenceGitSourceType(StrEnum):
    GIT = "git"

    def __str__(self) -> str:
        return str(self.value)
