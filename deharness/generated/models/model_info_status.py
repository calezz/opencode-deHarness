from enum import StrEnum

class ModelInfoStatus(StrEnum):
    ACTIVE = "active"
    ALPHA = "alpha"
    BETA = "beta"
    DEPRECATED = "deprecated"

    def __str__(self) -> str:
        return str(self.value)
