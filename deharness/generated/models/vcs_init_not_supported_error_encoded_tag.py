from enum import StrEnum

class VcsInitNotSupportedErrorEncodedTag(StrEnum):
    VCSINITNOTSUPPORTEDERROR = "VcsInitNotSupportedError"

    def __str__(self) -> str:
        return str(self.value)
