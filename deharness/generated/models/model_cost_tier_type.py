from enum import StrEnum

class ModelCostTierType(StrEnum):
    CONTEXT = "context"

    def __str__(self) -> str:
        return str(self.value)
