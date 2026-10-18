from enum import StrEnum

class ConnectionEnvInfoType(StrEnum):
    ENV = "env"

    def __str__(self) -> str:
        return str(self.value)
