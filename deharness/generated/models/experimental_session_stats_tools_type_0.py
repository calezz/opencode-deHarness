from enum import StrEnum

class ExperimentalSessionStatsToolsType0(StrEnum):
    DETAIL = "detail"
    NONE = "none"
    SUMMARY = "summary"

    def __str__(self) -> str:
        return str(self.value)
