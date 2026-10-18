from enum import StrEnum

class FileNotFoundErrorEncodedTag(StrEnum):
    FILENOTFOUNDERROR = "FileNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
