import sys
import os
try:
	import requests
except ImportError:
	os.system('pip install requests')

from os import system, name
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps
try:
	from websocket import create_connection
except ImportError:
	os.system('pip install websocket-client')
try:
	import pyfiglet
except:
	os.system('pip install pyfiglet')
try:
	import time
except:
	os.system('pip install time')
try:
	import telebot
except:
	os.system('pip install telebot')
try:
	import rich
except:
	os.system('pip install rich')

############################
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
G = '\033[2;36m'
E = '\033[1;31m'
V = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
#C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
R = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
O = '\x1b[38;5;208m' #برتقالي
BL = '\x1b[38;5;21m' #ازاق طوخ
YU = '\x1b[38;5;200m' #وردي طوخ
G = '\033[1;32m'
R = '\033[1;31m'
############################
#يخمط يذكر مصدر
class SafeUMAutomation:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.failed = 0
        self.success = 0
        self.retry = 0
        self.accounts = []

    def create_username(self):
        return choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(
            choices(list('qwertyuioplkjhgfdsazxcvbnm1234567890'), k=8)
        )

    def send_telegram_message(self, message):#ويووووووووو
        tlg = f"<code>{message}</code>"
        requests.post(f"https://api.telegram.org/bot{self.token}/sendmessage?chat_id={self.chat_id}&text=" + str(tlg),
                      params={'parse_mode': 'HTML'})

    def work(self):
        username = self.create_username()
        try:
            con = create_connection(
                'wss://193.200.173.45/Auth',  # اتصالات s1
                headers={
                    "app": "com.safeum.android",
                    "host": None,
                    "remoteIp": "195.13.182.213",
                    "remotePort": str(8080),
                    "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                    "time": "2024-09-19 11:00:00",
                    "url": "wss://193.200.173.45/Auth"
                },
                sslopt={"cert_reqs": CERT_NONE}
            )

            con.send(dumps({
                "action": "Register",
                "subaction": "Desktop",
                "locale": "ar_IQ",
                "gmt": "+03",
                "password": {
                    "m1x": "d9515a3ed09c5483b01aa29508b96e689814172b77a82decd8c628814abe6707",
                    "m1y": "7020e3e7386fc62c0af2b77e24ffad5a707992df67776060d7112392b1dff6d4",
                    "m2": "7ef4160c4e60101bcca5840a182cfbf62617564049c56d63efb3aa10e5c0ff14",
                    "iv": "fee4a7c512a79edef17bc9dd11f56e57",
                    "message": "a47083681e87ea0c47a1287ab52183152c308703e5f36da05860253e6d02dbd1bf85867106ab2d8b9d25c5b3356f005afc7fb645c560d5da9dc15b3dbc0bd868547e51f40c5498f158e2def932a3bbe4"
                },#اتصالت s1 يخمط يذكر مصدر
                "magicword": {
                    "m1x": "b61059a94268b3b37a249e929444bf1f08ca7907f0e53403031105de5d6893e1",
                    "m1y": "ae646038752cebecc8589ace4a661fccf3d98efcb07cf5c3524bb81bf620e5f8",
                    "m2": "0b5a12ef43f255f5aa2a33433fea00d8c7493cff5fc0433ad8b754083cda6a27",
                    "iv": "d558098e59ea01cad938588291d6e430",
                    "message": "07c413175a140b9c9ae671577980711a"
                },
                "magicwordhint": "0000",
                "login": str(username),
                "devicename": "Realme RMX3269",#اتصالات s1
                "softwareversion": "1.1.0.1640",
                "nickname":  "kwhdushdin",
                "os": "AND",
                "deviceuid": "f7a88f3e39abf27a",
                "devicepushuid": "*dlLBWfiMTwK7HK93_BfeJR:APA91bEcS5CUgFFieZMyCRw_mg2_nCp_hZm_OSTYro6LaYwau17KMdBgZDx0orW5YwqqAINCDmLn2EnH2Bh3ucK2gGZAZh6CjGtLDPpSmy3z2p9Ypw5hPJNU1lllEriq1BCY-y_HeVBX",
                "osversion": "and_11.0.0",
                "id": "953397628"
            }))

            gzip = decompress(con.recv()).decode('utf-8')

            if '"status":"Success"' in gzip:
                self.success += 1
                self.accounts.append(username)
                self.send_telegram_message(username)
                with open('users.txt', 'a') as f:
                    f.write(f'{username}\n')
                    #اتصللاتs1
            else:
                self.failed += 1

        except Exception:
            self.retry += 1

    def run(self):
        start = ThreadPoolExecutor(max_workers=10000)

        
        while True:
            start.submit(self.work)  
            sys.stdout.write(f'\r\033[92mSuccess: {self.success}\033[0m  '
                             f'\033[91mFailed: {self.failed}\033[0m '
                             f'\033[93mReTry: {self.retry}\033[0m')
            sys.stdout.flush()
            system("cls" if name == "nt" else "clear")


if __name__ == "__main__":
    figlet_text = pyfiglet.figlet_format("s1 & Zuess")
    print(figlet_text)
    print('_'*60)
    token =input(f'{Z}Enter your token : {M}')
    chat_id = input(f'{X}Enter your id : {G}')
    automation = SafeUMAutomation(token, chat_id)
    automation.run()
    #s1&zuess#+++++علي