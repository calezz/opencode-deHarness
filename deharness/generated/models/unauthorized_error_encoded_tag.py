from enum import StrEnum

class UnauthorizedErrorEncodedTag(StrEnum):
    UNAUTHORIZEDERROR = "UnauthorizedError"

    def __str__(self) -> str:
        return str(self.value)
