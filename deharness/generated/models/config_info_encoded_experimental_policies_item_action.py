from enum import StrEnum

class ConfigInfoEncodedExperimentalPoliciesItemAction(StrEnum):
    INTEGRATION_USE = "integration.use"
    PROVIDER_USE = "provider.use"
    TOOL_USE = "tool.use"

    def __str__(self) -> str:
        return str(self.value)
