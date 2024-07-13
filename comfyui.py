from typing import Any

from core.tools.errors import ToolProviderCredentialValidationError
from core.tools.provider.builtin.comfyui.tools.disney_style_cartoon import DisneyStyleCartoonTool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController


class ComfyUIProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            DisneyStyleCartoonTool.fork_tool_runtime(
                runtime={
                    "credentials": credentials,
                }
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
    