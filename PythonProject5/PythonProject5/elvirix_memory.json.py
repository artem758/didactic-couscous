import json
import logging

logger = logging.getLogger(__name__)
MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.info("memory.json не найден — создаём новый")
    except json.JSONDecodeError as e:
        logger.error(f"Невалидный JSON в {MEMORY_FILE}: {e}")
    return {}

def save_memory(mem):
    try:
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(mem, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.error(f"Не удалось сохранить память: {e}")

def run():
    mem = load_memory()
    logger.info(f"elvirix_memory: память загружена, записей — {len(mem)}")