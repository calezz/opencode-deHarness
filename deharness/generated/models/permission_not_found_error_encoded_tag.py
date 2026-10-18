from enum import StrEnum

class PermissionNotFoundErrorEncodedTag(StrEnum):
    PERMISSIONNOTFOUNDERROR = "PermissionNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
