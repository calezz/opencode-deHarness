from enum import StrEnum

class FormExternalFieldType(StrEnum):
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
