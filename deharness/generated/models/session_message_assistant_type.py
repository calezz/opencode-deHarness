from enum import StrEnum

class SessionMessageAssistantType(StrEnum):
    ASSISTANT = "assistant"

    def __str__(self) -> str:
        return str(self.value)
