from enum import StrEnum

class FormMultiselectFieldType(StrEnum):
    MULTISELECT = "multiselect"

    def __str__(self) -> str:
        return str(self.value)
