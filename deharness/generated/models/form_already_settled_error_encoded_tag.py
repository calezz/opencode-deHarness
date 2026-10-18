from enum import StrEnum

class FormAlreadySettledErrorEncodedTag(StrEnum):
    FORMALREADYSETTLEDERROR = "FormAlreadySettledError"

    def __str__(self) -> str:
        return str(self.value)
