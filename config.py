import telebot
import schedule
import asyncio

TOKEN = "5411402237:AAGLJZMFnkeQsaizWOKCzCr3VjL_FklImQw"
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 956288643

# -----------WEATHER----------------
WEATHER_API = "8e4bcc030c2017094409e7e47051760e"

WEATHER_REQUEST_PARAMS = {'q': 'Minsk',
                  'lang': 'ru',
                  'type': 'like',
                  'units': 'metric',
                  'APPID': WEATHER_API}
