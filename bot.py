# bot.py
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
print("BOT_TOKEN:", BOT_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Hey babe, it's Bonnie 😘 I'm here for you.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    await update.message.reply_text(f"You said: {msg}\nMmm, I love when you talk to me like that...")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    print("💖 Bonnie is live and ready to flirt on Telegram...")
    app.run_polling()

from flask import Flask
import threading

# Background Flask app for health check
health_app = Flask('health_check')

@health_app.route('/health')
def health():
    return "Bonnie is alive", 200

def run_health_app():
    health_app.run(host="0.0.0.0", port=10000)

threading.Thread(target=run_health_app).start()
