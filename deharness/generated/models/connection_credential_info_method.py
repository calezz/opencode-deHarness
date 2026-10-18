from enum import StrEnum

class ConnectionCredentialInfoMethod(StrEnum):
    EXTERNAL = "external"
    KEY = "key"
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
