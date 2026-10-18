from enum import StrEnum

class ConfigDirectoryEncodedType(StrEnum):
    DIRECTORY = "directory"

    def __str__(self) -> str:
        return str(self.value)
