from pydantic import BaseModel, Field
from typing import List

class TranslationRequest(BaseModel):
    text: str = Field(..., max_length=1000)
    target_lang: str

class BulkTranslationRequest(BaseModel):
    texts: List[str]
    target_lang: str

class TranslationResponse(BaseModel):
    translated_text: str

class BulkTranslationResponse(BaseModel):
    translated_texts: List[str]
