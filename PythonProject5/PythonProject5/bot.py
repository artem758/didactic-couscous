import time
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

try:
    import yaml
    from telegram import Update
    from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
    from elvirix_llm import generate_reply
    from elvirix_selfcheck import load_groups, check_group_transition
except ImportError as e:
    logger.critical(f"bot: не хватает зависимости {e}")
    raise

# Загрузка конфига
with open("config.yaml", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

TOKEN = cfg["telegram_token"]
GROUP_ID = cfg.get("group_id")
INTERVAL = cfg.get("reply_interval", 7200)
GROUP_LIST = load_groups()

last_ts = 0
counter = 0

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_ts, counter, GROUP_ID
    if str(update.effective_chat.username) != GROUP_ID:
        return
    now = time.time()
    if now - last_ts < INTERVAL:
        return
    reply = generate_reply(update.message.text)
    await update.message.reply_text(reply)
    last_ts = now
    counter += 1
    if counter >= 10:
        next_group = check_group_transition(GROUP_ID, GROUP_LIST)
        if next_group:
            GROUP_ID = next_group
            counter = 0
            await update.message.reply_text(f"🛰 Эльвирикс переходит в {GROUP_ID}")
        else:
            logger.warning("bot: нет групп для переключения")

def run():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    logger.info("bot: запускаю Telegram-бота")
    app.run_polling()