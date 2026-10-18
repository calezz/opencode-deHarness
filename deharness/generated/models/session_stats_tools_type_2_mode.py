from enum import StrEnum

class SessionStatsToolsType2Mode(StrEnum):
    DETAIL = "detail"

    def __str__(self) -> str:
        return str(self.value)
