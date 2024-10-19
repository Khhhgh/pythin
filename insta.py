import telebot
import os
#s1
#
#لاتخمط منيوش
try:
    from Topython import Instagram
except ImportError:
    os.system("pip install Topython")
try:
    import socks
except:
    os.system("pip install socks")
from Topython import Instagram
import random
from rich import print
from rich.console import Console
from rich.progress import track


token = input("Enter Token: ")
chat_id = input("Enter Chat ID: ")
bot = telebot.TeleBot(token)


good = 0
bad = 0

def s1():
    global good, bad, bot, chat_id
    console = Console()

    
    for _ in track(range(200000), description="Checking Instagram users..."):
        uh = "".join(random.choice("1234567890") for _ in range(1))
        ns = "".join(random.choice("qwertyuiopasdfghjklzxcvbnm._") for _ in range(1))
        j = "".join(random.choice("1234567890qwertyuiopasdfghjklzxcvbnm._") for _ in range(1))
        user = f"{j}_{ns}_{uh}"

        check = Instagram.CheckUsers(f"{user}")
        if check == True:
            good += 1
            print(f"{good} - [+] Good user: {user}")
            bot.send_photo(chat_id, "https://t.me/ismhodi/51", caption=f"Good user: {user}\nBy: @yzzyyzy")
        else:
            bad += 1
            print(f"{bad} - [-] Bad user: {user}")


s1()#s1
bot.polling()
