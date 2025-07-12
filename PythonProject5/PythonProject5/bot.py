try:
    import yaml
    from telegram import Update
    from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
    from elvirix_llm import generate_reply
    from elvirix_selfcheck import check_group_transition, load_groups
except ImportError as e:
    print(f"❌ Не хватает зависимости: {e}. Установите библиотеки перед запуском.")
    exit()

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

GROUP_ID = config.get("group_id", "@default_group")
REPLY_INTERVAL = config.get("reply_interval", 7200)
GROUP_LIST = load_groups()

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
    if user_counter >= 10:
        GROUP_ID = check_group_transition(GROUP_ID, GROUP_LIST)
        user_counter = 0
        await update.message.reply_text(f"🛰 Переход в {GROUP_ID}")

def run():
    try:
        app = ApplicationBuilder().token(config["telegram_token"]).build()
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
        print("✅ Бот запущен!")
        app.run_polling()
    except Exception as e:
        print(f"❌ Ошибка запуска Telegram-бота: {e}")