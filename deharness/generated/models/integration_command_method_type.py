from enum import StrEnum

class IntegrationCommandMethodType(StrEnum):
    COMMAND = "command"

    def __str__(self) -> str:
        return str(self.value)
