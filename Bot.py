from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_USERNAME = "https://t.me/vsbshhsee"

async def video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video

    msg = await context.bot.send_video(
        chat_id=CHANNEL_USERNAME,
        video=video.file_id
    )

    link = f"https://t.me/{CHANNEL_USERNAME[1:]}/{msg.message_id}"

    await update.message.reply_text(
        f"✅ Video Link:\n{link}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.VIDEO, video_handler))
app.run_polling()
