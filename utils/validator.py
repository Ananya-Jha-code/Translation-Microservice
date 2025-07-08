# Supported language ISO codes
SUPPORTED_LANGS = {"hi", "ta", "kn", "bn"}

def validate_lang(code: str) -> bool:
    return code in SUPPORTED_LANGS
