from enum import StrEnum

class RpcInternalErrorEncodedTag(StrEnum):
    RPCINTERNALERROR = "RpcInternalError"

    def __str__(self) -> str:
        return str(self.value)
