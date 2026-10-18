from enum import StrEnum

class SessionMessageShellStatus(StrEnum):
    EXITED = "exited"
    KILLED = "killed"
    RUNNING = "running"
    TIMEOUT = "timeout"

    def __str__(self) -> str:
        return str(self.value)
