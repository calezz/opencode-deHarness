from enum import StrEnum

class ProviderNotFoundErrorEncodedTag(StrEnum):
    PROVIDERNOTFOUNDERROR = "ProviderNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
