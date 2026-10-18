from enum import StrEnum

class FormStateType1Status(StrEnum):
    ANSWERED = "answered"

    def __str__(self) -> str:
        return str(self.value)
