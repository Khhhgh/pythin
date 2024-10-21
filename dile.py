import os
import requests
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps
import telebot
import rich

try:
    from websocket import create_connection
except ImportError:
    os.system("pip install websocket-client")
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []

token = input("Enter your token : ")
ID = input("Enter id : ")
os.system("clear")


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
        if con:
            con.send(dumps(
                {"action":"Register","subaction":"Desktop","locale":"ar_IQ","gmt":"+03",
                "password":{
                    "m1x":"46a0cc9a4a2d7dbfdd415b638c5ac75785296a20a4571db9c35d42e7765030d6",
                    "m1y":"6fc876d64d39e6a9c8528858c6c58790ffe391a85031e1beeedfc9a05b423d19",
                    "m2":"c658dd95d3e71d3fb98bee64d27021c82dcb692688a9a7e6e12cd20a713febef",
                    "iv":"2d7641484cefab364ef72cb8e506776b",
                    "message":"34a4b9ab724d2eacdb830b624eb25f279e39a688e055b5d2cc7896d7cef2890a40ff1dab419f72ee0e3219e596699f324b058a8bb16eeb666fc4313a9f67a451d9c0f97c76adbe3d399f9c1d5ca35076"
                },
                "magicword":{
                    "m1x":"69b4e070d334eddf3f1b1fec292e0033e0bdf7600128e93fc344f34220be79c1",
                    "m1y":"73324600ea0ccf0ec86e848a588d259101edacf5bfea8dedf67b14bb28195a17",
                    "m2":"e37836d84d4d3d13044ccb11d08de656f5ad74a4feaa5ed661bda755fa65da5a",
                    "iv":"1332b589b45b34a8478eed7f9cf2afe7",
                    "message":"9353adfad15789b4351236fb4a5b2fd0"},
                "magicwordhint":"0000",
                "login":str(username),
                "devicename":"Realme RMX3269",
                "softwareversion":"1.1.0.1640",
                "nickname":"uyggfgghhczdv",
                "os":"AND",
                "deviceuid":"f7a88f3e39abf27a",
                "devicepushuid":"*cME2FmjeSj6-869LtFwnwI:APA91bGyMZ_7-tmCzlep7Fz_mWJ9AnTimC83urrBkFMXxTpZhD7Q2xBpUc4DFJIUcKzfzI9H5SqZ0_sY36rc1QJd61kprv7iHSyHtELbuPVTPBbdE75qqs6eTaCoBpmRL_i6RTZEYbFF",
                "osversion":"and_11.0.0",
                "id":"1569606004"}
            ))

            response = decompress(con.recv()).decode("utf-8")
            if '"status":"Success"' in response:
                success += 1
                accounts.append(username)
                with open('users.txt', 'a') as file:
                    file.write(username + "\n")
                msg = f"{username}"
                url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}"
                requests.post(url)
            else:
                failed += 1
        con.close()
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
        + "Retry : "
        + str(retry)
    )
    if success >= 2900:
        print("Created Accounts Successfully Sent To Owner Group")

    if success > 0:
        z = "\n".join(accounts)
        print("\n", z)

    os.system("clear")