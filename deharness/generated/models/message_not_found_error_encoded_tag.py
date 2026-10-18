from enum import StrEnum

class MessageNotFoundErrorEncodedTag(StrEnum):
    MESSAGENOTFOUNDERROR = "MessageNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
