from enum import StrEnum

class InvalidCursorErrorEncodedTag(StrEnum):
    INVALIDCURSORERROR = "InvalidCursorError"

    def __str__(self) -> str:
        return str(self.value)
