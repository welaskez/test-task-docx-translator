from pydantic import BaseModel


class TranslateBody(BaseModel):
    text: str


class TranslateResponse(BaseModel):
    translated_text: str
