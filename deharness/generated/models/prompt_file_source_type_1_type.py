from enum import StrEnum

class PromptFileSourceType1Type(StrEnum):
    URI = "uri"

    def __str__(self) -> str:
        return str(self.value)
