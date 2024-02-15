from telegram.ext import(
    Updater, MessageHandler, CommandHandler, Filters
)

import logging
from settings import TOKEN

logging.basicConfig(filename='error_bot.log', level=logging.INFO)


def activate_bot():
    # Создаем бота
    bot = Updater(TOKEN, use_context=True)
    dp = bot.dispatcher

    # Задаем основные команды
    dp.add_handler(CommandHandler('start', hello_user))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('convert', convert_currency))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Бесконечный запуск бота (Ctrl + C для остановки)
    bot.start_polling()
    bot.idle


if __name__ == '__main__':
    activate_bot()
