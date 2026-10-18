from enum import StrEnum

class ShellInfoStatus(StrEnum):
    EXITED = "exited"
    KILLED = "killed"
    RUNNING = "running"
    TIMEOUT = "timeout"

    def __str__(self) -> str:
        return str(self.value)
