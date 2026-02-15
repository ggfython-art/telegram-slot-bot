import os
import random
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()

symbols = ["🍒", "🍋", "🍇", "7️⃣"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎰 Добро пожаловать в слот! Напиши /spin")

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = [random.choice(symbols) for _ in range(3)]
    text = " | ".join(result)
    
    if result.count(result[0]) == 3:
        text += "\n🔥 Джекпот!"
    else:
        text += "\n😢 Попробуй ещё!"

    await update.message.reply_text(text)

def main():
    keep_alive()
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CommandHandler("spin", spin))
    app_bot.run_polling()

if __name__ == "__main__":
    main()
