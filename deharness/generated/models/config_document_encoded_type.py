from enum import StrEnum

class ConfigDocumentEncodedType(StrEnum):
    DOCUMENT = "document"

    def __str__(self) -> str:
        return str(self.value)
