from enum import StrEnum

class FormNumberFieldType(StrEnum):
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
