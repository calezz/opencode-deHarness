from enum import StrEnum

class SessionMessageAssistantTextType(StrEnum):
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
