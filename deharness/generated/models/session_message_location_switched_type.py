from enum import StrEnum

class SessionMessageLocationSwitchedType(StrEnum):
    LOCATION_SWITCHED = "location-switched"

    def __str__(self) -> str:
        return str(self.value)
