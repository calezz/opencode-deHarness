from enum import StrEnum

class SessionMessageAssistantReasoningType(StrEnum):
    REASONING = "reasoning"

    def __str__(self) -> str:
        return str(self.value)
