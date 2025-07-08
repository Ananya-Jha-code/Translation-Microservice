from fastapi import APIRouter, HTTPException
from models.schemas import (
    TranslationRequest,
    TranslationResponse,
    BulkTranslationRequest,
    BulkTranslationResponse
)
from services.translator import translate_text, bulk_translate
from utils.logger import log_request
from utils.validators import validate_lang

router = APIRouter()

@router.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    if not validate_lang(request.target_lang):
        raise HTTPException(status_code=400, detail="Invalid language code.")
    
    translated = await translate_text(request.text, request.target_lang)
    log_request(request.text, request.target_lang, translated)
    return {"translated_text": translated}

@router.post("/translate/bulk", response_model=BulkTranslationResponse)
async def translate_bulk(request: BulkTranslationRequest):
    if not validate_lang(request.target_lang):
        raise HTTPException(status_code=400, detail="Invalid language code.")
    
    translations = await bulk_translate(request.texts, request.target_lang)
    for orig, trans in zip(request.texts, translations):
        log_request(orig, request.target_lang, trans)
    
    return {"translated_texts": translations}
