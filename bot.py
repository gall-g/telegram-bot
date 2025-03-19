from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Текст сообщения
    message_text = "Добро пожаловать! Нажмите кнопку ниже, чтобы открыть Mini App."

    # Создаем кнопку с ссылкой на Mini App
    keyboard = [
        [InlineKeyboardButton("📌 Купить/Продать", web_app={'url': 'https://gall-g.github.io/-/'})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text(message_text, reply_markup=reply_markup)

# Основная функция
async def main():
    # Вставьте ваш токен
    token = '7657252097:AAGcgwd145LnYPR00DTdk5m5va0xtqt2gzc'
    
    # Создаем приложение
    application = Application.builder().token(token).build()

    # Регистрация обработчика команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    await application.run_polling()

# Запуск асинхронной функции
if __name__ == '__main__':
    # Получаем текущий цикл событий
    loop = asyncio.get_event_loop()
    
    # Если цикл уже запущен, используем его
    if loop.is_running():
        # Создаем задачу для запуска бота
        task = loop.create_task(main())
        
        # Ожидаем завершения задачи (или прерывания)
        try:
            loop.run_until_complete(task)
        except asyncio.CancelledError:
            print("Бот остановлен.")
    else:
        # Если цикл не запущен, запускаем его
        loop.run_until_complete(main())
