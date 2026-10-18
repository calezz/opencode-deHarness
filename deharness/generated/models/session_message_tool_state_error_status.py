from enum import StrEnum

class SessionMessageToolStateErrorStatus(StrEnum):
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
