from enum import StrEnum

class ProviderEncoding(StrEnum):
    GZIP = "gzip"
    NONE = "none"
    ZSTD = "zstd"

    def __str__(self) -> str:
        return str(self.value)
