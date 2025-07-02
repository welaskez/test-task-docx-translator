from core.dependencies.services import TranslationServiceDep
from core.enums.trasnaltes import TranslationType
from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from starlette import status

router = APIRouter(prefix="/translates", tags=["Translates"])


@router.post(
    path="/docx",
    response_class=FileResponse,
    status_code=status.HTTP_200_OK,
)
async def translate_docx(
    translation_service: TranslationServiceDep,
    translation_type: TranslationType,
    document: UploadFile,
):
    return await translation_service.translate_docx(file=document, translation_type=translation_type)
