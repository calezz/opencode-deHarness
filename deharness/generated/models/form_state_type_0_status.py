from enum import StrEnum

class FormStateType0Status(StrEnum):
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
