from enum import StrEnum

class VcsBaseSource(StrEnum):
    DEFAULT = "default"
    REFLOG = "reflog"

    def __str__(self) -> str:
        return str(self.value)
