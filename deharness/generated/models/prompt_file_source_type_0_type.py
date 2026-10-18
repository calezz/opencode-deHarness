from enum import StrEnum

class PromptFileSourceType0Type(StrEnum):
    INLINE = "inline"

    def __str__(self) -> str:
        return str(self.value)
