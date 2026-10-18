from enum import StrEnum

class ProviderCompactionType1Type(StrEnum):
    NATIVE = "native"

    def __str__(self) -> str:
        return str(self.value)
