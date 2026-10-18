from enum import StrEnum

class FormBooleanFieldType(StrEnum):
    BOOLEAN = "boolean"

    def __str__(self) -> str:
        return str(self.value)
