from enum import StrEnum

class McpRemoteConfigEncodedType(StrEnum):
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
