from enum import StrEnum

class IntegrationExternalMethodType(StrEnum):
    EXTERNAL = "external"

    def __str__(self) -> str:
        return str(self.value)
