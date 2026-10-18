from enum import StrEnum

class InvalidRequestErrorEncodedTag(StrEnum):
    INVALIDREQUESTERROR = "InvalidRequestError"

    def __str__(self) -> str:
        return str(self.value)
