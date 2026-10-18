from enum import StrEnum

class AgentNotFoundErrorEncodedTag(StrEnum):
    AGENTNOTFOUNDERROR = "AgentNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
