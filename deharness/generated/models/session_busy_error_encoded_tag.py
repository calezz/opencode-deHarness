from enum import StrEnum

class SessionBusyErrorEncodedTag(StrEnum):
    SESSIONBUSYERROR = "SessionBusyError"

    def __str__(self) -> str:
        return str(self.value)
