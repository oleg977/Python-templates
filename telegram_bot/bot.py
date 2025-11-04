from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "ВСТАВЬ_СВОЙ_ТОКЕН"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот-шаблон 🚀")


def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
