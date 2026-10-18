from enum import StrEnum

class FormStringFieldType(StrEnum):
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
