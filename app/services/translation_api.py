from core.enums.trasnaltes import TranslationType
from core.schemas.translation_service import TranslateResponse
from httpx import AsyncClient


class TranslationAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._client = AsyncClient(base_url=base_url)

    async def translate(self, translation_type: TranslationType) -> TranslateResponse:
        response = await self._client.post(url=f"/translate/{translation_type}")
        return TranslateResponse.model_validate(response.json())
