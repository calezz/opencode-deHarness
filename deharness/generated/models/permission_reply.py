from enum import StrEnum

class PermissionReply(StrEnum):
    ALWAYS = "always"
    ONCE = "once"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)
