from enum import StrEnum

class RpcInternalErrorEncodedType(StrEnum):
    RPC_INTERNAL = "rpc.internal"
    RPC_INVALID_OUTPUT = "rpc.invalid_output"

    def __str__(self) -> str:
        return str(self.value)
