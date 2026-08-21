from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("سلام رامین اینجا هستم!")

async def profile(update, context):
    await update.message.reply_text("پروفایل مدیر")

def main():
    app = ApplicationBuilder().token("71031452").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profile", profile))

    app.run_polling()

if __name__ == "__main__":
    main()
