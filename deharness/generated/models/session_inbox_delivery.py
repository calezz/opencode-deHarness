from enum import StrEnum

class SessionInboxDelivery(StrEnum):
    QUEUE = "queue"
    STEER = "steer"

    def __str__(self) -> str:
        return str(self.value)
