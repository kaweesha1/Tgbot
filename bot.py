from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ⚠️ Security note:
# Public place එකකට token දාන්න එපා. Use env variable if possible.
BOT_TOKEN = "5058040730:AAGerUSFE0ZbXYdYZ0866bLTDRmEBF7DTLY"


# /start command (link එකෙන් open කරන වෙලාවට)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return

    if context.args:
        file_id = context.args[0]
        await update.message.reply_video(video=file_id)
    else:
        await update.message.reply_text("📹 Video එක upload කරන්න")


# video upload handler
