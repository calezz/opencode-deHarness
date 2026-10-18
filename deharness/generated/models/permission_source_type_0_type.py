from enum import StrEnum

class PermissionSourceType0Type(StrEnum):
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
