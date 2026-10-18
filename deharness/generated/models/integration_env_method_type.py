from enum import StrEnum

class IntegrationEnvMethodType(StrEnum):
    ENV = "env"

    def __str__(self) -> str:
        return str(self.value)
