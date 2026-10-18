from enum import StrEnum

class ReferenceLocalSourceType(StrEnum):
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
