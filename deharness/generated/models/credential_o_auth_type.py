from enum import StrEnum

class CredentialOAuthType(StrEnum):
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
