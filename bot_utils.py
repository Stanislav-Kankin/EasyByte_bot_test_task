import requests
import json
from settings import API_CURRENCY


# Получаем коэффициент для расчета валюты
def get_exchabge_rate(from_valute: str, to_valute: str) -> float:
    url = (
        f'https://currate.ru/api/?get=rates&pairs={from_valute}{to_valute}&key={API_CURRENCY}'
        )

    # Отправляем GET запрос на получение курсов валют
    response = requests.get(url)

    # Получаем данные в формате JSON
    data = json.loads(response.text)
    exchange_rate = data['data'][from_valute + to_valute]
    return float(exchange_rate)


# Приветствуем пользователя
def hello_user(update, context) -> None:
    name = update.message.from_user.first_name
    update.message.reply_text(
        f'Привет, {name}! Я бот для конвертации валют.\n'
        f'Введите /help для получения списка команд.'
        )


# Определяем команду для получения информации о доступных командах
def help_command(update, context) -> None:
    update.message.reply_text(
        f'Доступные команды:\n'
        f'/convert <сумма> <исходная_валюта> - <целевая_валюта> - Конвертировать валюту\n'
        f'/help - Справка'
        )


# Определяем команду для конвертации валюты
def convert_currency(update, context) -> None:
    # Получаем команду и параметры
    command = update.message.text.split()
    amount = float(command[1])
    from_currency = command[2].upper()
    to_currency = command[4].upper()
    result = amount * get_exchabge_rate(
        from_currency, to_currency
    )
    print(result, amount, from_currency, to_currency, end='\n')
    # # Отвечаем пользователю результатом конвертации
    update.message.reply_text(
        f'{amount} {from_currency} = {result} {to_currency}'
        )


# Определяем функцию для обработки простых текстовых сообщений
def echo(update, context) -> None:
    text = update.message.text
    if 'привет' in text.lower():
        update.message.reply_text('Привет!')
    elif 'пока' in text.lower():
        update.message.reply_text('До свидания!')
    else:
        update.message.reply_text('Не понимаю ваш запрос. Введите /help для получения списка команд.')
