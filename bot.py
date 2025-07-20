import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask
import threading

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram Command Handler
async def start(update, context):
    await update.message.reply_text("Bonnie is alive, my love.")

# Main runner
async def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    await app.run_polling()

# Health check server
health_app = Flask(__name__)

@health_app.route('/health')
def health():
    return "Bonnie is alive", 200

def run_health_app():
    health_app.run(host="0.0.0.0", port=10000)

# Start Flask in background
threading.Thread(target=run_health_app).start()

# Start Telegram bot loop
asyncio.run(run_bot())
