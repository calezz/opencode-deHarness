from enum import StrEnum

class FormStringFieldFormat(StrEnum):
    DATE = "date"
    DATE_TIME = "date-time"
    EMAIL = "email"
    URI = "uri"

    def __str__(self) -> str:
        return str(self.value)
