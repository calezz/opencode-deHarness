from enum import StrEnum

class RpcErrorEncodedTag(StrEnum):
    RPCERROR = "RpcError"

    def __str__(self) -> str:
        return str(self.value)
