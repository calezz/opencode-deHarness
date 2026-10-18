from enum import StrEnum

class SessionInboxUserType(StrEnum):
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
