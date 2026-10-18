from enum import StrEnum

class FormWhenOp(StrEnum):
    EQ = "eq"
    NEQ = "neq"

    def __str__(self) -> str:
        return str(self.value)
