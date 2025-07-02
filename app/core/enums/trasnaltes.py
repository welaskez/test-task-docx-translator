from enum import StrEnum


class TranslationType(StrEnum):
    RU_TO_KZ = "ru-kk"
    KZ_TO_RU = "kk-ru"


class FileExtensionType(StrEnum):
    DOCX = "docx"
