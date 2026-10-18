from enum import StrEnum

class LocationNotFoundErrorEncodedTag(StrEnum):
    LOCATIONNOTFOUNDERROR = "LocationNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
