from enum import StrEnum

class ProviderCompactionType0Type(StrEnum):
    SUMMARY = "summary"

    def __str__(self) -> str:
        return str(self.value)
