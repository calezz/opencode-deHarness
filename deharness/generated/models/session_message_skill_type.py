from enum import StrEnum

class SessionMessageSkillType(StrEnum):
    SKILL = "skill"

    def __str__(self) -> str:
        return str(self.value)
