from enum import StrEnum

class ConnectionCredentialInfoType(StrEnum):
    CREDENTIAL = "credential"

    def __str__(self) -> str:
        return str(self.value)
