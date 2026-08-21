from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "8784120583:AAGzTDjx0aH-wEnNoinjCP8Ooklf_i3l3Ys"
ADMIN_ID = 71031452

async def start(update, context):
    await update.message.reply_text("سلام! پیامت رو به رامین بگو.")

async def forward_to_admin(update, context):
    user = update.message.from_user
    text = update.message.text

    # ارسال پیام کاربر برای تو
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"پیام از {user.first_name}:\n{text}"
    )

    # جواب به کاربر
    await update.message.reply_text("پیامت برای رامین ارسال شد.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, forward_to_admin))

app.run_polling()
