import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ---- Keep alive web server (for Replit + UptimeRobot) ----
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=8080)

Thread(target=run_web).start()
# ---------------------------------------------------------

BOT_TOKEN = os.environ.get("8518142175:AAHtMpTE4I6DtCOZNS4KvjtgoOaTtEUB-t8")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Send me a video.\nI will convert it to a download link."
    )

# When user sends a video
async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video

    file_id = video.file_id

    file = await context.bot.get_file(file_id)

    # Telegram direct file link
    download_link = file.file_path

    await update.message.reply_text(
        f"✅ Your video download link:\n\n{download_link}"
    )

def main():
    app_bot = ApplicationBuilder().token(8518142175:AAHtMpTE4I6DtCOZNS4KvjtgoOaTtEUB-t8).build()

    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.VIDEO, handle_video))

    print("Bot started...")
    app_bot.run_polling()

if __name__ == "__main__":
    main()
