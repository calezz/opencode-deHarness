from enum import StrEnum

class ProjectNotFoundErrorEncodedTag(StrEnum):
    PROJECTNOTFOUNDERROR = "ProjectNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
