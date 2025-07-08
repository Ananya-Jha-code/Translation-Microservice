from datetime import datetime

# In-memory log store
log_store = []

def log_request(original: str, lang: str, translated: str):
    log_store.append({
        "timestamp": datetime.utcnow().isoformat(),
        "original": original,
        "language": lang,
        "translated": translated
    })
