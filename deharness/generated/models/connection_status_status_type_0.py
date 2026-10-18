from enum import StrEnum

class ConnectionStatusStatusType0(StrEnum):
    NEEDS_AUTH = "needs_auth"

    def __str__(self) -> str:
        return str(self.value)
