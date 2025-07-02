from typing import Annotated

from fastapi import Depends
from services.translates_service import TranslatesService
from services.translation_api import TranslationAPI

from core.config import settings


def get_translates_service() -> TranslatesService:
    translation_api = TranslationAPI(base_url=settings.translation_api.base_url)
    return TranslatesService(translation_api)


TranslationServiceDep = Annotated[TranslatesService, Depends(get_translates_service)]
