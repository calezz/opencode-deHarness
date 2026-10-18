from enum import StrEnum

class ModelCacheFormat(StrEnum):
    ALIBABA = "alibaba"
    ANTHROPIC = "anthropic"

    def __str__(self) -> str:
        return str(self.value)
