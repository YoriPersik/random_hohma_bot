import os
import random

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


# 🔐 Токен нашего бота
TOKEN = "hohma"


# 📁 Папка с мемами
MEMES_FOLDER = "memes"


async def meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет случайный мем."""

    # Получаем список файлов из папки memes
    files = [
        file
        for file in os.listdir(MEMES_FOLDER)
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp"))
    ]

    # Если мемов нет
    if not files:
        await update.message.reply_text("У меня закончились мемы 😭")
        return

    # Выбираем случайный мем
    random_meme = random.choice(files)

    # Отправляем его
    with open(os.path.join(MEMES_FOLDER, random_meme), "rb") as photo:
        await update.message.reply_photo(photo=photo)


def main():
    # Создаём приложение бота
    application = Application.builder().token(TOKEN).build()

    # Команда /meme
    application.add_handler(CommandHandler("meme", meme))

    # Запускаем бота
    print("Бот запущен! Нажми Ctrl+C для остановки.")

    application.run_polling()


if __name__ == "__main__":
    main()