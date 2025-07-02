__all__ = ("router",)

from fastapi import APIRouter

from .translates import router as translates_router

router = APIRouter(prefix="/v1")
router.include_router(translates_router)
