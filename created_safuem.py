import os
import requests
from os import system
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except ImportError:
    system("pip install websocket-client")
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []

token = ''
ID = ''


def work():
    global failed, success, retry
    username = choice("qwertyuioasdfghjklzxcvbnpm1234567890") + "".join(
        choices(list("qwertyuioasdfghjklzxcvbnpm1234567890"), k=12)
    )
    try:
        con = create_connection(
            "wss://51.79.208.190:8080/Reg",
            header=[
                "app: com.safeum.android",
                "host: None",
                "remoteIp: 51.79.208.190",
                "remotePort: 8080",
                "sessionId: None",
                "time: 2024-04-11 11:00:00",
                "url: wss://51.79.208.190:8080/Reg",
            ],
            sslopt={"cert_reqs": CERT_NONE},
        )
        con.send(dumps(
            {"action": "Register", "subaction": "Desktop", "locale": "ar_IQ", "gmt": "+03",
             "password": {
                 "m1x": "374af193b54778c0d80ac468c951a42e0d10f725fb02cc041214762f8a898aba",
                 "m1y": "ffb2a997e103ac6e81cb303a75c4e301a6a6220fc62484ae86fa75d72a964784",
                 "m2": "77b3a653c63e87455489164118e0f53abcd046627a4bc98ed4d78d622b6a504a",
                 "iv": "48538eae910a4312e60c58b548e2ddfb",
                 "message": "c9521c3fa92082a37afd13cf656efea72d7addd3d610e7912a6b3f76225409c332922699123552fc46d78f0b3d0066b8b6a872842421738596d0cc3db62fcb981d4c5db2daa63e6ad85b6aa9d2365738"},
             "magicword": {
                 "m1x": "1256bc123862e728457912be864250d29c467e818cd95454e630f2ebaeefa614",
                 "m1y": "d644820bd65efc04eca9555011ee6076ba398bb9684d527bf32eb46f78aca015",
                 "m2": "60a99a889ba3908566a380e175415be2fd60f48f3b42badb5b5538932f50a71b",
                 "iv": "bde381fc92ef94d0c2d4126f9ae4bfaf",
                 "message": "ffaa2877c9ada8f6cca8be71e956367f"},
             "magicwordhint": "0000",
             "login": str(username),
             "devicename": "Realme RMX3269",
             "softwareversion": "1.1.0.1640",
             "nickname": "ddsdddddfffssfg",
             "os": "AND",
             "deviceuid": "f7a88f3e39abf27a",
             "devicepushuid": "*cmYJInBNTz2cdJ9qsDYOR6:APA91bE52gpn43VAA6EZB7IZRknHEliAG_TUbChb3ApMNGuVAENWHuSwpc5qT6jZVEFIyKM_H44weSKvmdkBlJZ8CKfCYTnW8WpxaI0nN6gdv1W_YFadyqlY2Hn3CxvkBn9D2DjMPPAd",
             "osversion": "and_11.0.0", "id": "109181025"}
        ))

        response = decompress(con.recv()).decode("utf-8")
        if '"status":"Success"' in response:
            success += 1
            accounts.append(username + " : anoo | @O_An0.")
            with open('accs.txt', 'a') as file:
                file.write(username + "\n")
            msg = f"{username}"
            url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}"
            requests.post(url)
        else:
            failed += 1
    except Exception as e:
        print(f"Error: {e}")
        retry += 1


start = ThreadPoolExecutor(max_workers=1000)

while True:
    start.submit(work)
    print(
        "\n\n\n"
        + " " * 25
        + "Success : "
        + str(success)
        + "\n\n\n"
        + " " * 25
        + "Failed : "
        + str(failed)
        + "\n\n\n"
        + " " * 25
        + "ReTry : "
        + str(retry)
    )
    if success >= 1000:
        print("Created Accounts Successfully Sent To Owner Group")

    if success > 0:
        z = "\n".join(accounts)
        print("\n", z)

    os.system("clear")