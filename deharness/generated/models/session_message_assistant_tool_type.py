from enum import StrEnum

class SessionMessageAssistantToolType(StrEnum):
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
