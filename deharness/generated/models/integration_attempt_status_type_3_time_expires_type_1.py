from enum import StrEnum

class IntegrationAttemptStatusType3TimeExpiresType1(StrEnum):
    INFINITY = "Infinity"
    NAN = "NaN"
    VALUE_1 = "-Infinity"

    def __str__(self) -> str:
        return str(self.value)
