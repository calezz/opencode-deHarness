from enum import StrEnum

class ToolFileContentType(StrEnum):
    FILE = "file"

    def __str__(self) -> str:
        return str(self.value)
