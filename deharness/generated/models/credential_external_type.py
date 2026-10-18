from enum import StrEnum

class CredentialExternalType(StrEnum):
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
