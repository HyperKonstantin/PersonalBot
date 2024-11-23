import asyncio

import schedule

from config import *
from telebot.types import Message
import requests
from decorators import *

scheduler_working = False
weather_sending_time = "05:40"


@bot.message_handler(commands=["weather"])
@for_chats(ADMIN_ID)
def send_weather(message: Message):
    print(message.from_user)
    params = message.text.strip().split()[1:]
    if len(params) == 0:
        bot.send_message(message.chat.id, "Отсутствуют параметры")
        return

    match params[0]:
        case 'help':
            weather_help(message.chat.id)
        case 'now':
            send_weather_message(message.chat.id)
        case 'setschedtime':
            set_scheduler_time(params[1:], message.chat.id)
        case 'startsched':
            start_scheduler(message.chat.id)
        case 'stopsched':
            stop_scheduler(message.chat.id)


def weather_help(chat_id):
    bot.send_message(chat_id, """
*now* - будет ли сегодня дождь

*setschedtime* <hh:mm> - установить время отправки сообщений (пример: setschedtime 08:00)

*startsched* - включить автоматическую отправку сообщений

*stopsched* - выключить автоматическую отправку сообщений
    """, parse_mode='Markdown')

def set_scheduler_time(params, chat_id):
    global weather_sending_time
    weather_sending_time = params[0]
    bot.send_message(chat_id, f"Время отправки сообщений: {weather_sending_time}")


def start_scheduler(chat_id):
    # schedule.every().day.at(weather_sending_time).do(lambda: send_weather_message(message.chat.id))
    schedule.every(10).seconds.do(lambda: print("schedule"))
    asyncio.run(scheduler_pulling())
    bot.send_message(chat_id, "шедулер запущен")


def stop_scheduler(chat_id):
    global scheduler_working
    scheduler_working = False
    bot.send_message(chat_id, "шедулер остановлен")


def send_weather_message(chat_id):
    response = requests.get("http://api.openweathermap.org/data/2.5/find", params=WEATHER_REQUEST_PARAMS).json()
    is_rain = any(list(map(lambda x: x['rain'], response["list"])))

    if is_rain:
        bot.send_message(chat_id, "Сегодня возможен дождь!")
    else:
        bot.send_message(chat_id, "Дождя не ожидается")



async def scheduler_pulling():
    global scheduler_working
    scheduler_working = True

    while scheduler_working:
        schedule.run_pending()
        print("scheduler work")
        await asyncio.sleep(5)
