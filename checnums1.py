import telebot
from telebot import types
from telethon import TelegramClient
from telethon.errors import PhoneNumberBannedError
import asyncio

tok = '7915967893:AAERfb3HxG0GHDGC4I36mNY9VMC6YZTrWXA'
bot = telebot.TeleBot(tok)

@bot.message_handler(commands=['start'])
def start_handler(message):
    id = message.from_user.id
    button_check = types.InlineKeyboardButton(text="بدء فحص رقم", callback_data="check_number")
    button_dev = types.InlineKeyboardButton(text="مطور", url="https://t.me/yzzyyzy")
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(button_check, button_dev)
    
    bot.reply_to(message, """
    ها اضغط على زر حتى نفحص رقم محظور لو لا
    """, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query_handler(call):
    if call.data == "check_number":
        bot.send_message(call.message.chat.id, "أرسل لي الرقم لفحصه.")
        bot.register_next_step_handler(call.message, check_number)


def check_number(message):
    num = message.text.strip()
    
    async def check(num):
        api_id = 25217515
        api_hash = "1bb27e5be73593e33fc735c1fbe0d855"
        client = TelegramClient('S1', api_id, api_hash)
        await client.connect()

        try:
            await client.send_code_request(num)
            bot.send_message(message.chat.id, "الرقم غير محظور.")
        except PhoneNumberBannedError:
            bot.send_message(message.chat.id, "الرقم محظور.")
        finally:
            await client.disconnect()
        
    asyncio.run(check(num))

bot.polling()