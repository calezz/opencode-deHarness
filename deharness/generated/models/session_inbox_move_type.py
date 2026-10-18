from enum import StrEnum

class SessionInboxMoveType(StrEnum):
    MOVE = "move"

    def __str__(self) -> str:
        return str(self.value)
