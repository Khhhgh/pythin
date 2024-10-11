import os
try:
    from telebot import types
    import telebot  # Importing telebot
except ImportError:  # Fixed 'expext' to 'except'
    os.system("pip install pyTelegramBotAPI")  # Correct package name

# Initialize the bot
token = "7229675132:AAHDvs6KnAvNEQf10lEw9e9-O64L9k7objg"  # Add your bot token here
bot = telebot.TeleBot(token)

# Handler for '/start' command
@bot.message_handler(commands=['start'])
def s1(message):  
    user_id = message.from_user.id  # 'id' variable is not used, so you can remove it or keep it for further use
    c = types.InlineKeyboardButton(text="def", url="https://t.me/yzzyyzy")  # Fixed incorrect URL format
    x = types.InlineKeyboardButton(text="ابدا مضرطه قصدي حفظ ماتزسلع بي ملف", callback_data="x")  # Correct callback data
    s = types.InlineKeyboardMarkup(row_width=1)  # Correct markup initialization
    s.add(c, x)
    bot.reply_to(message, "ها عمي اهلا بك في بوت ماتزسله يحفظه يي ملف يفيد كسوليني", reply_markup=s)  # Corrected bot reply

# Callback query handler
@bot.callback_query_handler(func=lambda call: True)
def sqqq(call):
    bot.edit_message_text("ارسل حسابات لي كي حفظها بي ملف واسرلها الك", call.message.chat.id, call.message.message_id)
    
    file = call.message.text
    with open("users.txt", "a") as d:  # Removed 'l=' (which was incorrect)
        d.write(file + "\n")
    
    # Send the file back as a document
    bot.send_document(call.message.chat.id, open("users.txt", "rb"))  # Fixed file sending logic

# Start polling
bot.infinity_polling()  # Corrected typo