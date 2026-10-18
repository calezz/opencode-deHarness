from enum import StrEnum

class CredentialKeyType(StrEnum):
    KEY = "key"

    def __str__(self) -> str:
        return str(self.value)
