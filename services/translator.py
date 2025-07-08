# You can later replace this mock with Google Translate API calls

MOCK_TRANSLATIONS = {
    "hello": {
        "hi": "नमस्ते",
        "ta": "வணக்கம்",
        "kn": "ಹಲೋ",
        "bn": "হ্যালো"
    },
    "goodbye": {
        "hi": "अलविदा",
        "ta": "விடைபெறு",
        "kn": "ವಿದಾಯ",
        "bn": "বিদায়"
    }
}

async def translate_text(text: str, target_lang: str) -> str:
    word = text.lower().strip()
    return MOCK_TRANSLATIONS.get(word, {}).get(target_lang, f"[Translated:{text}]")

async def bulk_translate(texts: list, target_lang: str) -> list:
    return [await translate_text(text, target_lang) for text in texts]
