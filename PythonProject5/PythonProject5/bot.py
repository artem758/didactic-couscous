import time

try:
    import yaml
    from telegram import Update
    from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
    from elvirix_llm import generate_reply
    from elvirix_selfcheck import load_groups, check_group_transition
except ImportError as e:
    print(f"❌ Отсутствует зависимость: {e}. Установите библиотеки.")
    exit()

try:
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
except Exception as e:
    print(f"❌ Не удалось загрузить config.yaml: {e}")
    exit()

GROUP_ID = config.get("group_id", "@default_group")
GROUP_LIST = load_groups()
REPLY_INTERVAL = config.get("reply_interval", 7200)

last_reply_time = 0
user_counter = 0

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global last_reply_time, user_counter, GROUP_ID
    if str(update.effective_chat.username) != GROUP_ID:
        return
    now = time.time()
    if now - last_reply_time < REPLY_INTERVAL:
        return
    reply = generate_reply(update.message.text)
    await update.message.reply_text(reply)
    last_reply_time = now
    user_counter += 1
    if user_counter >= 10 and GROUP_LIST:
        GROUP_ID = check_group_transition(GROUP_ID, GROUP_LIST)
        user_counter = 0
        await update.message.reply_text(f"🔄 Переход Эльвирикс в группу {GROUP_ID}")

def run():
    try:
        app = ApplicationBuilder().token(config["telegram_token"]).build()
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
        print("✅ Эльвирикс запущен в Telegram")
        app.run_polling()
    except Exception as e:
        print(f"❌ Ошибка запуска Telegram-бота: {e}")