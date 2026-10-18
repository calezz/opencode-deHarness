from enum import StrEnum

class ExperimentalMigrationV1StatusResponse200Type0Status(StrEnum):
    COMPLETED = "completed"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
