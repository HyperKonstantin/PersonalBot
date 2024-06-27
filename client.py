import time

from config import *
from parser import *
from telebot.types import *


@bot.message_handler(commands=["start"])
def start(message : Message):
    bot.send_message(message.chat.id, f"Ботик воркает")
    houses_count_monitoring(message)


def houses_count_monitoring(message : Message):
    generator = selenium_parser()
    houses_count = 0
    while True:
        new_houses_count = next(generator)

        if new_houses_count > houses_count:
            print("---- New house! ----")
            houses_count = new_houses_count
            bot.send_message(message.chat.id, f"Новое объявление (теперь их {houses_count})!!!")
            time.sleep(2)
            bot.send_message(message.chat.id, "Не пропусти!!!")
            time.sleep(2)
            bot.send_message(message.chat.id, "давай, звони!!!")

        elif new_houses_count < houses_count:
            print("---- Minus House ----")
            houses_count = new_houses_count
            bot.send_message(message.chat.id, "Объявление пропало 😢")

        print(f"[{datetime.now()}] -- count: {houses_count}")
        time.sleep(60)
