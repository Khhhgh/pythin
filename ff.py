import telebot
from telebot import types

token="حط هنا توكنك"
bot = telebot.TeleBot(token)
owner_id = #حط هينا ايدي مالج بوت يعني ايديك 
admins = [owner_id]   

def admin_panel(message):
    markup = types.InlineKeyboardMarkup()
    send_message_all = types.InlineKeyboardButton("اذاعة 🥹", callback_data="send_all")
    send_message_user = types.InlineKeyboardButton("إرسال رسالة لمستخدم", callback_data="send_user")
    ban_user = types.InlineKeyboardButton("حظر مستخدم", callback_data="ban_user")
    add_admin = types.InlineKeyboardButton("إضافة أدمن", callback_data="add_admin")
    user_count = types.InlineKeyboardButton("احصائيات", callback_data="user_count")

    markup.add(send_message_all, send_message_user)
    markup.add(ban_user, add_admin)
    markup.add(user_count)

    
    bot.send_message(message.chat.id, "ها ولاك ", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    
    clean_users_file()

    
    if not is_user_registered(user_id, username):
        
        with open("users.txt", "a") as f:
            f.write(f"ID: {user_id}, Username: {username}, Full Name: {full_name}\n")


    
    if user_id in admins:
        admin_panel(message)


def is_user_registered(user_id, username):
    with open("users.txt", "r") as f:
        users = f.readlines()
        for user in users:
            if f"ID: {user_id}" in user or f"Username: {username}" in user:
                return True
    return False


def clean_users_file():
    with open("users.txt", "r") as f:
        users = f.readlines()

    unique_users = []
    seen_ids = set()
    seen_usernames = set()

    for user in users:
        user_id = user.split(",")[0].split(":")[1].strip()
        username = user.split(",")[1].split(":")[1].strip()

        
        if user_id not in seen_ids and username not in seen_usernames:
            unique_users.append(user)
            seen_ids.add(user_id)
            seen_usernames.add(username)

    
    with open("users.txt", "w") as f:
        f.writelines(unique_users)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "send_all":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="أرسل الرسالة التي تريد إرسالها لجميع المستخدمين:")
        bot.register_next_step_handler(call.message, send_message_to_all)
    elif call.data == "send_user":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="أدخل معرف المستخدم لإرسال الرسالة إليه:")
        bot.register_next_step_handler(call.message, ask_user_id)
    elif call.data == "ban_user":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="أدخل معرف المستخدم لحظره:")
        bot.register_next_step_handler(call.message, ban_user)
    elif call.data == "add_admin":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="أدخل معرف المستخدم لإضافته كأدمن:")
        bot.register_next_step_handler(call.message, add_admin)
    elif call.data == "user_count":
        user_count = get_user_count()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"عدد مستخدمي البوت: {user_count}")


def send_message_to_all(message):
    msg_text = message.text
    with open("users.txt", "r") as f:
        users = f.readlines()
        for user in users:
            user_id = int(user.split(",")[0].split(":")[1].strip())
            bot.send_message(user_id, msg_text)
    bot.send_message(message.chat.id, "تم إرسال الرسالة للجميع!")
def ask_user_id(message):
    user_id = message.text
    bot.send_message(message.chat.id, "أدخل الرسالة التي تريد إرسالها:")
    bot.register_next_step_handler(message, lambda msg: send_message_to_user(msg, user_id))


def send_message_to_user(message, user_id):
    try:
        bot.send_message(int(user_id), message.text)
        bot.send_message(message.chat.id, f"تم إرسال الرسالة إلى المستخدم {user_id}")
    except:
        bot.send_message(message.chat.id, "حدث خطأ أثناء إرسال الرسالة. تأكد من معرف المستخدم.")


def ban_user(message):
    user_id = message.text
    with open("banned_users.txt", "a") as f:
        f.write(f"{user_id}\n")
    bot.send_message(message.chat.id, f"تم حظر المستخدم {user_id}")


def add_admin(message):
    new_admin_id = int(message.text)
    if new_admin_id not in admins:
        admins.append(new_admin_id)
        bot.send_message(message.chat.id, f"تم إضافة المستخدم {new_admin_id} كأدمن.")
    else:
        bot.send_message(message.chat.id, "هذا المستخدم هو أدمن بالفعل.")


def get_user_count():
    with open("users.txt", "r") as f:
        users = f.readlines()
    return len(users)


@bot.message_handler(func=lambda message: True)
def forward_message_to_owner(message):
    with open("banned_users.txt", "r") as f:
        banned_users = f.read().splitlines()

    if str(message.from_user.id) in banned_users:
        bot.send_message(message.chat.id, "لقد تم حظرك من استخدام هذا البوت.")
    elif message.from_user.id == owner_id or message.from_user.id in admins:
        bot.send_message(message.reply_to_message.forward_from.id, message.text)
    else:
        bot.forward_message(owner_id, message.chat.id, message.message_id)

bot.infinity_polling()