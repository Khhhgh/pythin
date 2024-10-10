import telebot
from telebot import types


token = "7229675132:AAHDvs6KnAvNEQf10lEw9e9-O64L9k7objg"
bot = telebot.TeleBot(token)


owner_id = 5583353259


@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name
    with open("users.txt", "a") as f:
        f.write(f"ID: {user_id}, Username: {username}\n")
    
    
    bot.reply_to(message, f"""
    أهلاً [{full_name}](https://t.me/{username}) بك في بوت تواصل المحظورين خاصة لي S1
    أرسل رسالتك وسيرد عليك المالك قريباً،،،😢😢😢
    """, parse_mode="Markdown")


@bot.message_handler(func=lambda message: True)
def forward_message_to_owner(message):
    
    if message.from_user.id == owner_id:
        
        bot.send_message(message.reply_to_message.forward_from.id, message.text)
    else:
        
        bot.forward_message(owner_id, message.chat.id, message.message_id)


bot.infinity_polling()