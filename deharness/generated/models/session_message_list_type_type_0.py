from enum import StrEnum

class SessionMessageListTypeType0(StrEnum):
    AGENT_SWITCHED = "agent-switched"
    ASSISTANT = "assistant"
    COMPACTION = "compaction"
    LOCATION_SWITCHED = "location-switched"
    MODEL_SWITCHED = "model-switched"
    SHELL = "shell"
    SKILL = "skill"
    SYNTHETIC = "synthetic"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
