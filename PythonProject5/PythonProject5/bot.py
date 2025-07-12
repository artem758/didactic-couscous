import time
import yaml
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

from elvirix_lm import generate_reply
from elvirix_selfcheck import check_group_transition

# Загрузка конфигурации
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

GROUP_ID = config["group_id"]
GROUP_LIST = config["group_list"]
REPLY_INTERVAL = config["reply_interval"]

last_reply_time = 0
user_counter = 0

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_reply_time, user_counter, GROUP_ID

    if str(update.effective_chat.id) != GROUP_ID:
        return

    now = time.time()
    if now - last_reply_time < REPLY_INTERVAL:
        return

    text = update.message.text
    reply = generate_reply(text)

    await update.message.reply_text(reply)
    last_reply_time = now

    user_counter += 1
    if user_counter >= 10:
        GROUP_ID = check_group_transition(GROUP_ID, GROUP_LIST)
        user_counter = 0
        await update.message.reply_text("🛰 Переход в новую группу завершён!")

# Запуск приложения
app = ApplicationBuilder().token(config["telegram_token"]).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
app.run_polling()