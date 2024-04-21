import telebot
from bot_token import TOKEN 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text']
)

def echo(message):
    bot.send_message(message.chat.id, message.text *10)

if __name__ == '__main__':
    bot.infinity_polling()  