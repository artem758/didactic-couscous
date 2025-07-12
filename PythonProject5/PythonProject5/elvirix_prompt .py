import logging

logger = logging.getLogger(__name__)
PROMPT_FILE = "prompt.txt"

def load_prompt():
    try:
        with open(PROMPT_FILE, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        logger.warning(f"{PROMPT_FILE} не найден — используем пустой промпт")
    return ""

def run():
    prompt = load_prompt()
    logger.info(f"elvirix_prompt: загружен промпт, длина — {len(prompt)} симв.")