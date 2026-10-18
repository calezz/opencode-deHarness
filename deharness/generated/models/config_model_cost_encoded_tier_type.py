from enum import StrEnum

class ConfigModelCostEncodedTierType(StrEnum):
    CONTEXT = "context"

    def __str__(self) -> str:
        return str(self.value)
