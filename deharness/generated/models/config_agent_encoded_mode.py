from enum import StrEnum

class ConfigAgentEncodedMode(StrEnum):
    ALL = "all"
    PRIMARY = "primary"
    SUBAGENT = "subagent"

    def __str__(self) -> str:
        return str(self.value)
