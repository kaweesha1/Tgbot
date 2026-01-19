from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = "HTTP API:
8300609477:AAHM6Si6nkNSJrrsiexbVfb3FWKSpy3scgU"

# /start command (link open කරද්දි)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        file_id = context.args[0]
        await update.message.reply_video(video=file_id)
    else:
        await update.message.reply_text("Video එක upload කරන්න 📹")

# video upload handler
async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    file_id = video.file_id

    bot_username = context.bot.username
    link = f"https://t.me/{bot_username}?start={file_id}"

    await update.message.reply_text(
        f"✅ Video link ready:\n\n{link}\n\nමේ link එක share කරන්න."
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VIDEO, handle_video))

app.run_polling()
