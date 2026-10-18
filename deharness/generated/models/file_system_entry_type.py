from enum import StrEnum

class FileSystemEntryType(StrEnum):
    DIRECTORY = "directory"
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
