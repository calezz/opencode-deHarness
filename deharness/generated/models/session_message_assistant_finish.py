from enum import StrEnum

class SessionMessageAssistantFinish(StrEnum):
    CONTENT_FILTER = "content-filter"
    ERROR = "error"
    LENGTH = "length"
    STOP = "stop"
    TOOL_CALLS = "tool-calls"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
