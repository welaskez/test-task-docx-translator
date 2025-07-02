from core.enums.trasnaltes import TranslationType
from core.schemas.translation_api import TranslateBody, TranslateResponse
from fastapi import HTTPException
from httpx import AsyncClient
from starlette import status


class TranslationAPI:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._client = AsyncClient(base_url=base_url)

    async def translate(self, translation_type: TranslationType, text: str) -> TranslateResponse:
        await self.healthcheck()
        response = await self._client.post(
            url=f"/translate/{translation_type.value}/",
            json=TranslateBody(text=text).model_dump(),
            timeout=20.0,
        )
        return TranslateResponse.model_validate(response.json())

    async def healthcheck(self) -> None:
        response = await self._client.get(url="/")
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY, detail="Translation service is currently unavailable"
            )
