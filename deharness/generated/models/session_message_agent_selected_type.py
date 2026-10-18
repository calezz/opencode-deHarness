from enum import StrEnum

class SessionMessageAgentSelectedType(StrEnum):
    AGENT_SWITCHED = "agent-switched"

    def __str__(self) -> str:
        return str(self.value)
