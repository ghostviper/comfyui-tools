from typing import Any

from core.tools.errors import ToolProviderCredentialValidationError
from core.tools.provider.builtin.comfyui.tools.disney_style_cartoon import DisneyStyleCartoonTool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController


class ComfyUIProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        
        try:
            if 'base_url' not in credentials or not credentials.get('base_url'):
                raise ToolProviderCredentialValidationError("ComfyUI base url is required.")
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
    