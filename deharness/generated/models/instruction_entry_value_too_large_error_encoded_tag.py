from enum import StrEnum

class InstructionEntryValueTooLargeErrorEncodedTag(StrEnum):
    INSTRUCTIONENTRYVALUETOOLARGEERROR = "InstructionEntryValueTooLargeError"

    def __str__(self) -> str:
        return str(self.value)
