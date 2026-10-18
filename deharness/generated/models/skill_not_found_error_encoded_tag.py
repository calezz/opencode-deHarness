from enum import StrEnum

class SkillNotFoundErrorEncodedTag(StrEnum):
    SKILLNOTFOUNDERROR = "SkillNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
