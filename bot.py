from telegram.ext import (
    Updater, MessageHandler, CommandHandler, Filters
)

import logging
from settings import TOKEN
from bot_utils import (
    hello_user, help_command, convert_currency,
    echo
    )

# Логгируем, создаем файл
logging.basicConfig(filename='error_bot.log', level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
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
    main()
