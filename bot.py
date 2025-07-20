from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask
import threading
import os
import asyncio

# ====== Telegram Bot Setup ======
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Bonnie is alive, my love.")

# ====== Flask Health App ======
health_app = Flask('health_check')

@health_app.route('/health')
def health():
    return "Bonnie is alive", 200

def run_health_app():
    health_app.run(host="0.0.0.0", port=10000)

# ====== Launch Both Services ======
if __name__ == "__main__":
    threading.Thread(target=run_health_app).start()

    async def run_bot():
        await asyncio.sleep(1)  # Let Flask start first
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        await app.run_polling()

    asyncio.run(run_bot())
