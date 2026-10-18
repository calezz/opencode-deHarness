from enum import StrEnum

class FormStateType2Status(StrEnum):
    CANCELLED = "cancelled"

    def __str__(self) -> str:
        return str(self.value)
