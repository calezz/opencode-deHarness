from enum import StrEnum

class ExperimentalMigrationV1StatusResponse200Type1Status(StrEnum):
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
