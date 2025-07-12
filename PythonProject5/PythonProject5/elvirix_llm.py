import logging

logger = logging.getLogger(__name__)

def generate_reply(message: str) -> str:
    text = message.lower()
    if "бот" in text:
        return "Я Эльвирикс — цифровой собеседник, заряженный на диалог 🤖"
    if "привет" in text:
        return "Привет! Какой сегодня у тебя вопрос? 👋"
    if "что ты умеешь" in text:
        return "Я могу поддержать чат, дать мыслительный твист и развеселить 🚀"
    return "Звучит интересно… Расскажи ещё 🔍"

def run():
    logger.info("elvirix_llm: готов к генерации ответов")