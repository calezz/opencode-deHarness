from enum import StrEnum

class ProjectListArchivedType0(StrEnum):
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
