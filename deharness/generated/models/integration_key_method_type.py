from enum import StrEnum

class IntegrationKeyMethodType(StrEnum):
    KEY = "key"

    def __str__(self) -> str:
        return str(self.value)
