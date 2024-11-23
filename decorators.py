from config import *
def admin(func):
    def inner(message: telebot.types.Message):
        if message.from_user.id == ADMIN_ID:
            func(message)

    return inner


def for_chats(*chats):
    def outer(func):
        def inner(message: telebot.types.Message):
            if message.chat.id in chats:
                func(message)
        return inner
    return outer
