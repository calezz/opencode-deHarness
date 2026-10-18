from enum import StrEnum

class ToolTextContentType(StrEnum):
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
