from enum import StrEnum

class ExperimentalMigrationV1StatusResponse200Type2Status(StrEnum):
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
