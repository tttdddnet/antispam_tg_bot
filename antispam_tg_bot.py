import telebot

TOKEN = ""
GROUP_ID = 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: "abcdef.com" in message.text)
def handle_message(message):
    chat_id = message.chat.id
    message_id = message.message_id

    bot.delete_message(chat_id, message_id)
    #bot.send_message(chat_id, "Сообщение удалено")
                
bot.infinity_polling(timeout=10, long_polling_timeout = 5)
