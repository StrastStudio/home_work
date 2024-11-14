import telebot as tb
TOKEN = "8061173589:AAE-d5G9ZpWhH4nGXxRuNdyrogdmvN-tccM"

Bot = tb.TeleBot(TOKEN)

@Bot.message_handler(commands=["start"])
def start(message):
    Bot.send_message(message.chat.id, f"Здрастье {message.from_user.first_name}")

Bot.polling()