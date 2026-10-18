from enum import StrEnum

class ModelMaxTokensField(StrEnum):
    MAX_COMPLETION_TOKENS = "max_completion_tokens"
    MAX_TOKENS = "max_tokens"

    def __str__(self) -> str:
        return str(self.value)
