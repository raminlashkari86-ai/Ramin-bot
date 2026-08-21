from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask
import threading

# --- Telegram Bot ---
async def start(update, context):
    await update.message.reply_text("سلام رامین، ربات آنلاین روشنه")

async def profile(update, context):
    await update.message.reply_text("پروفایل مدیر")

def run_bot():
    app = ApplicationBuilder().token("8784120583:AAGzTDjx0aH-wEnNoinjCP8Ooklf_i3l3Ys").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("profile", profile))

    app.run_polling()

# --- Web Server for Render ---
web_app = Flask(__name__)

@web_app.route("/")
def home():
    return "Bot is running!"

def run_web():
    web_app.run(host="0.0.0.0", port=10000)

# --- Start both bot + web server ---
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_web()

