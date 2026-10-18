from enum import StrEnum

class ForbiddenErrorEncodedTag(StrEnum):
    FORBIDDENERROR = "ForbiddenError"

    def __str__(self) -> str:
        return str(self.value)
