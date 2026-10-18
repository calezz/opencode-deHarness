from enum import StrEnum

class SessionMessageUserType(StrEnum):
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
