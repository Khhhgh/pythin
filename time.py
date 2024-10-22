import os
os.system("pip install telebot")
import telebot
from telebot import types
from datetime import datetime
import threading

tok = input("Enter your token : ")
bot = telebot.TeleBot(tok)

admin_id = 5583353259
user_schedules = {}

def check_schedule():
    while True:
        now = datetime.now()
        for user_id, schedule in user_schedules.items():
            for entry in schedule:
                start_time = datetime.strptime(entry['start_time'], "%I:%M%p")
                end_time = datetime.strptime(entry['end_time'], "%I:%M%p")

                if now >= start_time and not entry['notified']:
                    bot.send_message(user_id, f"گوم اقره {entry['subject']} الآن!", reply_markup=get_done_button())
                    entry['notified'] = True

                if now >= end_time and not entry['finished']:
                    bot.send_message(user_id, f"انتهى وقت القراءة {entry['subject']}! هل ترغب بمراجعة؟", reply_markup=get_done_button())
                    entry['finished'] = True
        threading.Event().wait(60)

def get_done_button():
    markup = types.InlineKeyboardMarkup()
    done_button = types.InlineKeyboardButton(text="تمام", callback_data="done")
    markup.add(done_button)
    return markup

@bot.message_handler(commands=['start'])
def sta(mes):
    user_id = mes.from_user.id
    full_name = mes.from_user.full_name
    username = mes.from_user.username
    photo_id = None

    photos = bot.get_user_profile_photos(user_id)
    if photos.total_count > 0:
        photo_id = photos.photos[0][0].file_id

    n = types.InlineKeyboardButton(text="مطور", url="http://t.me/yzzyyzy")
    j = types.InlineKeyboardButton(text="إضافة مادة", callback_data="add_subject")
    z = types.InlineKeyboardMarkup(row_width=1)
    z.add(n, j)

    if photo_id:
        bot.send_photo(mes.chat.id, photo_id, caption=f"""
[{full_name}](http://t.me/{username}) ها هذا بوت تنظيم وقت يفيد جماعات سادس وجماعات وزاري
""", parse_mode="markdown", reply_markup=z)
    else:
        bot.send_message(mes.chat.id, f"""
[{full_name}](http://t.me/{username}) ها هذا بوت تنظيم وقت يفيد جماعات سادس وجماعات وزاري
""", parse_mode="markdown", reply_markup=z)

    if user_id == admin_id:
        admin_button = types.InlineKeyboardButton(text="لوحة الأدمن", callback_data="admin_panel")
        z.add(admin_button)
        bot.send_message(mes.chat.id, "مرحباً بالأدمن!", reply_markup=z)

@bot.callback_query_handler(func=lambda call: call.data == "admin_panel")
def admin_panel(call):
    if call.from_user.id == admin_id:
        markup = types.InlineKeyboardMarkup(row_width=2)
        broadcast_button = types.InlineKeyboardButton(text="إرسال رسالة جماعية", callback_data="broadcast")
        view_users_button = types.InlineKeyboardButton(text="عرض المستخدمين", callback_data="view_users")
        markup.add(broadcast_button, view_users_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="لوحة الأدمن:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "view_users")
def view_users(call):
    if call.from_user.id == admin_id:
        users_list = "\n".join([f"{user_id}: {len(schedule)} مواد" for user_id, schedule in user_schedules.items()])
        bot.send_message(call.message.chat.id, f"قائمة المستخدمين:\n{users_list}")

@bot.callback_query_handler(func=lambda call: call.data == "broadcast")
def broadcast_message(call):
    if call.from_user.id == admin_id:
        bot.send_message(call.message.chat.id, "أرسل الرسالة التي تريد إرسالها إلى جميع المستخدمين.")
        bot.register_next_step_handler(call.message, process_broadcast)

def process_broadcast(message):
    if message.from_user.id == admin_id:
        broadcast_text = message.text
        for user_id in user_schedules.keys():
            bot.send_message(user_id, f"رسالة من الأدمن:\n{broadcast_text}")
        bot.send_message(message.chat.id, "تم إرسال الرسالة إلى جميع المستخدمين.")

@bot.callback_query_handler(func=lambda call: call.data == "add_subject")
def add_subject(call):
    bot.send_message(call.message.chat.id, "أدخل المادة بتنسيق: مادة:بداية:نهاية (مثال: رياضيات:2pm:4pm)")

@bot.message_handler(func=lambda message: ":" in message.text)
def receive_subject(message):
    try:
        subject, start_time, end_time = message.text.split(":")
        start_time = datetime.strptime(start_time, "%I%p").strftime("%I:%M%p")
        end_time = datetime.strptime(end_time, "%I%p").strftime("%I:%M%p")

        user_id = message.from_user.id
        if user_id not in user_schedules:
            user_schedules[user_id] = []

        user_schedules[user_id].append({
            "subject": subject,
            "start_time": start_time,
            "end_time": end_time,
            "notified": False,
            "finished": False
        })

        bot.send_message(message.chat.id, f"تمت إضافة المادة: {subject} من {start_time} إلى {end_time}")
        schedule_markup = get_schedule_markup(user_id)
        bot.send_message(message.chat.id, "تم تحديث الجدول.", reply_markup=schedule_markup)

    except ValueError:
        bot.send_message(message.chat.id, "تنسيق غير صحيح! تأكد من استخدام التنسيق: مادة:بداية:نهاية")

def get_schedule_markup(user_id):
    markup = types.InlineKeyboardMarkup(row_width=1)

    if user_id in user_schedules:
        for entry in user_schedules[user_id]:
            button_text = f"{entry['subject']} - {entry['start_time']} إلى {entry['end_time']}"
            markup.add(types.InlineKeyboardButton(text=button_text, callback_data="ignore"))

    view_schedule_button = types.InlineKeyboardButton(text="عرض الجدول", callback_data="view_schedule")
    markup.add(view_schedule_button)

    return markup

@bot.callback_query_handler(func=lambda call: call.data == "view_schedule")
def view_schedule(call):
    user_id = call.from_user.id
    if user_id in user_schedules:
        schedule_markup = get_schedule_markup(user_id)
        bot.send_message(call.message.chat.id, "جدول المواد الحالي:", reply_markup=schedule_markup)
    else:
        bot.send_message(call.message.chat.id, "لم تقم بإضافة أي مواد حتى الآن.")

@bot.callback_query_handler(func=lambda call: call.data == "done")
def stop_notifications(call):
    bot.send_message(call.message.chat.id, "تم إيقاف التنبيهات لهذه المادة.")

threading.Thread(target=check_schedule, daemon=True).start()

bot.infinity_polling()