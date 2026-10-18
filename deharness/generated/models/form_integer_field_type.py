from enum import StrEnum

class FormIntegerFieldType(StrEnum):
    INTEGER = "integer"

    def __str__(self) -> str:
        return str(self.value)
