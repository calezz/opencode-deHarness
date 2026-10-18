from enum import StrEnum

class FormInvalidAnswerErrorEncodedTag(StrEnum):
    FORMINVALIDANSWERERROR = "FormInvalidAnswerError"

    def __str__(self) -> str:
        return str(self.value)
