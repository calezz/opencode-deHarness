from enum import StrEnum

class UnknownErrorEncodedTag(StrEnum):
    UNKNOWNERROR = "UnknownError"

    def __str__(self) -> str:
        return str(self.value)
