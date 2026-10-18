from enum import StrEnum

class SessionMessageModelSelectedType(StrEnum):
    MODEL_SWITCHED = "model-switched"

    def __str__(self) -> str:
        return str(self.value)
