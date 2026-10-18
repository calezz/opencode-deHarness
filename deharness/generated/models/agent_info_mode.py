from enum import StrEnum

class AgentInfoMode(StrEnum):
    ALL = "all"
    PRIMARY = "primary"
    SUBAGENT = "subagent"

    def __str__(self) -> str:
        return str(self.value)
