from pydantic import BaseModel


class TranslateResponse(BaseModel):
    translated_text: str
