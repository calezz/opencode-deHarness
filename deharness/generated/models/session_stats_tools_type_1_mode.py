from enum import StrEnum

class SessionStatsToolsType1Mode(StrEnum):
    SUMMARY = "summary"

    def __str__(self) -> str:
        return str(self.value)
