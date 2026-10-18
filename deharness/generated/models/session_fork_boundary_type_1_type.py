from enum import StrEnum

class SessionForkBoundaryType1Type(StrEnum):
    THROUGH = "through"

    def __str__(self) -> str:
        return str(self.value)
