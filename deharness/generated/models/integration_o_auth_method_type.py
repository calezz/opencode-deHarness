from enum import StrEnum

class IntegrationOAuthMethodType(StrEnum):
    OAUTH = "oauth"

    def __str__(self) -> str:
        return str(self.value)
