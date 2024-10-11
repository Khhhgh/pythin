from telebot import types
import os
import requests
from os import system
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

token=input("Enter your token")
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def s1(message):
    id = message.from_user.id
    a= types.InlineKeyboardButton(text="بدا انشاء حساب ",url="https//t.me@yzzyyzy")
    z = types.InlineKeyboardButton(text="بدا انشاء حساب ", callback_data="s")
    x = types.InlineKeyboardMarkup(row_width=1)
    x.add(z,a)
    bot.reply_to(message.id,"""ها هذا بوت انشاء حسابات سافيون اضغط على زر اسفل حتى ابدي اسوي حسابات ساقيوم
    """, reply_markup=x)


@bot.callback_query_handler(func=lambda call: True)
def xx(call):
    if call.data == "s":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="""
                          
                            
                           (   انتضر ائخي"""
        