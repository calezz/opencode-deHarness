from enum import StrEnum

class ModelReasoningFieldType0(StrEnum):
    REASONING = "reasoning"
    REASONING_CONTENT = "reasoning_content"
    REASONING_TEXT = "reasoning_text"

    def __str__(self) -> str:
        return str(self.value)
