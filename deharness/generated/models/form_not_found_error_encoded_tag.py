from enum import StrEnum

class FormNotFoundErrorEncodedTag(StrEnum):
    FORMNOTFOUNDERROR = "FormNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
