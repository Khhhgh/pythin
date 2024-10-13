from typing import Text
import telebot
from telebot import types
from collections import defaultdict
import time
from time import time
import websocket
import json
import requests
import pyrogram
import telethon
import datetime
import time
import hijri_converter
import random 
import os
import sys
user_message_count = defaultdict(int)
user_message_count=0


token = "7488755736:AAHoKPQISWUAZVZVJSMB8kPcdhBj53nn8Is"
bot = telebot.TeleBot(token)
number_of_ok=0
ok=types.InlineKeyboardButton(text=f"❤️{number_of_ok}",callback_data="ok")


def get_user_role(chat_id, user_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        status = member.status
        if status == 'creator':
            return "مالك المجموعة"
        elif status == 'administrator':
            return "مشرف"
        elif status == 'member':
            return "عضو عادي"
        elif status == 'restricted':
            return "مقيد"
        elif status == 'left':
            return "غادر المجموعة"
        elif status == 'kicked':
            return "محظور"
        else:
            return "غير معروف"
    except Exception as e:
        return f"حدث خطأ: {e}"

@bot.message_handler(func=lambda message: message.text == "رتبتي")
def send_user_role(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    role = get_user_role(chat_id, user_id)
    bot.send_message(chat_id, f"رتبتك في هذه المجموعة: {role}")



def is_admin(chat_id, user_id):
    """التحقق مما إذا كان المستخدم إداريًا أو مالكًا للمجموعة"""
    member = bot.get_chat_member(chat_id, user_id)
    return member.status in ['administrator', 'creator']

def get_admins_and_owner(chat_id):
    """استرجاع معرفات المدراء ومالك المجموعة"""
    admins = bot.get_chat_administrators(chat_id)
    owner_id = None
    for admin in admins:
        if admin.status == 'creator':
            owner_id = admin.user.id
    return owner_id

@bot.message_handler(commands=["start"])
def start_command(message):
    channels = ["@QBQQ2", "@QRQQ3"]
    user_id = message.from_user.id

    try:
        # تحقق من اشتراك المستخدم في القنوات
        if any(bot.get_chat_member(channel, user_id).status == "left" for channel in channels):
            buttons = [types.InlineKeyboardButton(channel, url=f"https://t.me/{channel[1:]}") for channel in channels]
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(*buttons)
            bot.send_message(message.chat.id, "عذراً عزيزي عليك الاشتراك في قنوات البوت 🗿", reply_markup=markup)
        else:
            buttons = [
                types.InlineKeyboardButton("مطور البوت", url="https://t.me/@yzzyyzy"),
                types.InlineKeyboardButton("أضفني لمجموعتك", url="http://t.me/z_z_s_bot?startgroup=new")
            ]
            markup = types.InlineKeyboardMarkup(row_width=1)
            markup.add(*buttons)
            bot.send_photo(message.chat.id, "https://t.me/QRQQ3/3", caption="""
            ✧︙أهلآ بك في بوت ماعرف شسمه
            ✧︙اختصاص البوت حماية المجموعات
            ✧︙لتفعيل البوت عليك اتباع مايلي ...
            ✧︙اضف البوت الى مجموعتك
            ✧︙ارفعه ادمن {مشرف}
            ✧︙ارسل كلمة { تفعيل } ليتم تفعيل المجموعه
            ✧︙معرف البوت ← {@z_z_s_bot}
            ✧︙مطور البوت ← {@yzzyyzy}
            """, reply_markup=markup)
    except Exception as e:
        pass
       

@bot.message_handler(func=lambda message: message.text == "طرد")
def kick_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if is_admin(chat_id, user_id):
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_first_name = message.reply_to_message.from_user.first_name
            target_user_name = message.reply_to_message.from_user.username
            try:
                bot.kick_chat_member(chat_id, target_user_id)
                bot.send_message(chat_id, f"[{target_first_name}](https://t.me/{target_user_name}): تم طرد هذا العضو بنجاح", parse_mode="Markdown", disable_web_page_preview=True)
            except Exception as e:
                bot.reply_to(message, "حدث خطأ أثناء محاولة طرد العضو.")
                print(f"Error in kick_user: {e}")
        else:
            bot.reply_to(message, "يرجى الرد على الرسالة التي تخص العضو المراد طرده🗿.")
    else:
        bot.reply_to(message, "ليس لديك رتبة ادمن.")
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime



# قوائم لتخزين معرفات المستخدمين المحظورين والمقيدين
banned_users = []
restricted_users = []

@bot.message_handler(func=lambda message: message.text.lower() == 'حظر' and message.reply_to_message)
def ban_user(message):
    if message.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(message.chat.id)]:
        banned_user_id = message.reply_to_message.from_user.id
        banned_user_username = message.reply_to_message.from_user.username
        banned_user_full_name = f"{message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name or ''}"

        try:
            bot.ban_chat_member(message.chat.id, banned_user_id)
            banned_users.append(banned_user_id)
            bot.reply_to(message, f"[{banned_user_full_name}](https://t.me/{banned_user_username}): تم حظر العضو بنجاح", parse_mode="Markdown", disable_web_page_preview=True)
        except Exception as e:
            bot.reply_to(message, f"حدث خطأ أثناء حظر العضو: {str(e)}")

@bot.message_handler(func=lambda message: message.text.lower() == 'إلغاء حظر' and message.reply_to_message)
def unban_user(message):
    if message.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(message.chat.id)]:
        unbanned_user_id = message.reply_to_message.from_user.id
        unbanned_user_username = message.reply_to_message.from_user.username
        unbanned_user_full_name = f"{message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name or ''}"

        try:
            bot.unban_chat_member(message.chat.id, unbanned_user_id)
            banned_users.remove(unbanned_user_id)
            bot.reply_to(message, f"[{unbanned_user_full_name}](https://t.me/{unbanned_user_username}): تم إلغاء حظر العضو بنجاح", parse_mode="Markdown", disable_web_page_preview=True)
        except Exception as e:
            bot.reply_to(message, f"حدث خطأ أثناء إلغاء الحظر: {str(e)}")

@bot.message_handler(func=lambda message: message.text.lower() == 'تقيد'and message.reply_to_message)
def restrict_user(message):
    if message.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(message.chat.id)]:
        restricted_user_id = message.reply_to_message.from_user.id
        restricted_user_username = message.reply_to_message.from_user.username
        restricted_user_full_name = f"{message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name or ''}"

        try:
            bot.restrict_chat_member(message.chat.id, restricted_user_id, can_send_messages=False)
            restricted_users.append(restricted_user_id)
            bot.reply_to(message, f"[{restricted_user_full_name}](https://t.me/{restricted_user_username}): تم تقييد العضو بنجاح", parse_mode="Markdown", disable_web_page_preview=True)
        except Exception as e:
            bot.reply_to(message, f"حدث خطأ أثناء تقييد العضو: {str(e)}")

@bot.message_handler(func=lambda message: message.text.lower() == 'إلغاء تقييد' and message.reply_to_message)
def unrestrict_user(message):
    if message.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(message.chat.id)]:
        unrestricted_user_id = message.reply_to_message.from_user.id
        unrestricted_user_username = message.reply_to_message.from_user.username
        unrestricted_user_full_name = f"{message.reply_to_message.from_user.first_name} {message.reply_to_message.from_user.last_name or ''}"

        try:
            bot.restrict_chat_member(message.chat.id, unrestricted_user_id, can_send_messages=True)
            restricted_users.remove(unrestricted_user_id)
            bot.reply_to(message, f"[{unrestricted_user_full_name}](https://t.me/{unrestricted_user_username}): تم إلغاء تقييد العضو بنجاح", parse_mode="Markdown", disable_web_page_preview=True)
        except Exception as e:
            bot.reply_to(message, f"حدث خطأ أثناء إلغاء التقييد: {str(e)}")
            
@bot.message_handler(func=lambda message: message.text.lower() == 'محظورين')
def list_banned_users(message):
    if message.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(message.chat.id)]:
        if not banned_users:
            bot.reply_to(message, "لا يوجد مستخدمين محظورين.")
            return

        user_list = "\n".join([f"[{bot.get_chat(banned_user).first_name}](https://t.me/{bot.get_chat(banned_user).username})" for banned_user in banned_users])
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("مسح المحظورين", callback_data="clear_banned"))

        bot.reply_to(message, f"قائمة المحظورين:\n{user_list}", reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text.lower() == 'المقيدين')
def list_restricted_users(message):
    if message.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(message.chat.id)]:
        if not restricted_users:
            bot.reply_to(message, "لا يوجد مستخدمين مقيدين.")
            return

        user_list = "\n".join([f"[{bot.get_chat(restricted_user).first_name}](https://t.me/{bot.get_chat(restricted_user).username})" for restricted_user in restricted_users])
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("مسح المقيدين", callback_data="clear_restricted"))

        bot.reply_to(message, f"قائمة المقيدين:\n{user_list}", reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "clear_banned")
def clear_banned(call):
    if call.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(call.message.chat.id)]:
        for banned_user_id in banned_users:
            try:
                bot.unban_chat_member(call.message.chat.id, banned_user_id)
            except Exception as e:
                bot.answer_callback_query(call.id, f"حدث خطأ: {str(e)}")
                return

        banned_users.clear()
        bot.edit_message_text("تم مسح جميع المحظورين.", chat_id=call.message.chat.id, message_id=call.message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "clear_restricted")
def clear_restricted(call):
    if call.from_user.id in [admin.user.id for admin in bot.get_chat_administrators(call.message.chat.id)]:
        for restricted_user_id in restricted_users:
            try:
                bot.restrict_chat_member(call.message.chat.id, restricted_user_id, can_send_messages=True)
            except Exception as e:
                bot.answer_callback_query(call.id, f"حدث خطأ: {str(e)}")
                return

        restricted_users.clear()
        bot.edit_message_text("تم مسح جميع المقيدين.", chat_id=call.message.chat.id, message_id=call.message.message_id)

# تشغيل 

@bot.message_handler(func=lambda message: message.text in ["قحبه", "فرخ", "منويج", "كس", "كسمك", "كس اختك", "كسمكم", "كسوامك", "كسمختك", "كسا/خت", "كسك", "fuke", "انيجك", "ابن كواد", "كواد", "راح انيج كس/ختك", "راح انيجك", "ها منويح", "كسكچ"])
def text_delete(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        user_id = message.from_user.id
        user_name = message.from_user.username
        full_name = message.from_user.full_name
        bot.send_message(message.chat.id, f"[{full_name}](https://t.me/{user_name}): ممنوع ارسال الفشار", parse_mode="Markdown", disable_web_page_preview=True)
    except Exception as e:
        print(f"Error deleting message: {e}")

from collections import defaultdict
from datetime import datetime
import random
import telebot
from telebot import types
from hijri_converter import Gregorian

# استبدل هذا بالتوكن الخاص ببوتك


# حالة التفعيل
activation_status = {}

user_message_count = defaultdict(int)
number_of_ok = 0

def get_user_role(chat_id, user_id):
    chat_member = bot.get_chat_member(chat_id, user_id)
    return chat_member.status

def check_user_message_count(user_id, user_message_count):
    if user_message_count[user_id] > 15000:
        return "ملك الشسمه"
    elif user_message_count[user_id] > 10000:
        return "كافي تحجي ابو شسمه"
    elif user_message_count[user_id] > 5000:
        return "شگد تحجي"
    elif user_message_count[user_id] > 1000:
        return "بدا يتحسن 😍"
    elif user_message_count[user_id] > 100:
        return "نايم كاعد"
    else:
        return "هل بل خير يابه"

@bot.message_handler(func=lambda message: message.text == "ايدي")
def send_idd(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # حساب عدد الرسائل
    user_message_count[user_id] += 1

    user_name = message.from_user.username if message.from_user.username else "غير متوفر"
    full_name = message.from_user.full_name

    # محاولة الحصول على البايو
    try:
        bio = bot.get_chat(message.from_user.id).bio
    except Exception:
        bio = "غير متوفر"

    role = get_user_role(chat_id, user_id)

    # احصل على صورة البروفايل
    profile_photos = bot.get_user_profile_photos(user_id)
    if profile_photos.total_count > 0:
        photo_file_id = profile_photos.photos[0][-1].file_id
        bot.send_photo(
            chat_id,
            photo_file_id,
            caption=(
                f"""
✧︙ايديك : ❨{user_id}❩
✧︙معرفك : ❨@{user_name}❩
✧‍︙رتبتك : ({role})
✧︙البايو : ❨{bio}❩
✧︙عدد الرسائل : ({user_message_count[user_id]})
✧︙تفاعلاك : {check_user_message_count(user_id, user_message_count)}
                """
            ),
            reply_to_message_id=message.message_id
        )
    else:
        bot.send_message(
            chat_id,
            f"""
✧︙ايديك : ❨{user_id}❩
✧︙معرفك : ❨@{user_name}❩
✧‍︙رتبتك : ({role})
✧︙البايو : ❨{bio}❩
✧︙عدد الرسائل : ({user_message_count[user_id]})
✧︙تفاعلاك : {check_user_message_count(user_id, user_message_count)}
            """,
            reply_to_message_id=message.message_id
        )

    # إنشاء لوحة أزرار
    ok = types.InlineKeyboardButton("OK", callback_data="ok")
    i = types.InlineKeyboardMarkup(row_width=1)
    i.add(ok)
    bot.send_message(message.chat.id, "", reply_markup=i)

@bot.callback_query_handler(func=lambda call: call.data == "ok")
def handle_callback(call):
    global number_of_ok
    number_of_ok += 1
    bot.answer_callback_query(call.id, f"عدد التفاعلات الآن: {number_of_ok}")
    bot.edit_message_reply_markup(
        call.message.chat.id,
        call.message.message_id,
        reply_markup=types.InlineKeyboardMarkup(row_width=1).add(
            types.InlineKeyboardButton(f"❤️ {number_of_ok}", callback_data="ok")
        )
    )

@bot.message_handler(func=lambda message: message.text.lower() == "بايو")
def handle_bio(message):
    try:
        # الحصول على معلومات العضو في المجموعة
        chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)

        # محاولة استخراج البايو
        bio = bot.get_chat(message.from_user.id).bio

        bot.send_message(message.chat.id, f"البايو الخاص بك: {bio}")
    except Exception as e:
        bot.send_message(message.chat.id, f"حدث خطأ: {str(e)}")

@bot.message_handler(func=lambda message: message.text == "تفعيل")
def handle_activation(message):
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)

    if chat_member.status in ["creator", "administrator"]:
        chat_id = message.chat.id
        chat_title = message.chat.title

        if chat_id in activation_status and activation_status[chat_id]:
            msg = f"{chat_title} مفعل بالفعل"
        else:
            activation_status[chat_id] = True
            msg = f"تم تفعيل البوت في {chat_title}"

        try:
            # الحصول على معلومات المجموعة بما في ذلك صورة المجموعة
            chat_info = bot.get_chat(chat_id)
            chat_photo = chat_info.photo

            if chat_photo:
                # إذا كانت هناك صورة للمجموعة، استخرج ملف ID الصورة الكبيرة
                photo_file_id = chat_photo.big_file_id
                bot.send_photo(chat_id=chat_id, photo=photo_file_id, caption=msg)
            else:
                bot.send_message(chat_id, msg)
        except Exception as e:
            bot.send_message(chat_id, f"حدث خطأ: {str(e)}")

@bot.message_handler(func=lambda message: message.text == "الوقت")
def send_time1(message):
    # الحصول على الوقت الحالي بتنسيق 24 ساعة
    current_time = datetime.now().strftime('%H:%M:%S')
    time_parts = current_time.split(':')  # تقسيم الوقت إلى أجزاء (ساعات، دقائق، ثوانٍ)

    # تحويل الساعات والدقائق والثواني إلى أرقام
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    # تحديد الفترة الزمنية (صباحًا/مساءً)
    period = current_period(hours)

    # تحويل الساعات إلى تنسيق 12 ساعة
    hours_12 = hours % 12
    if hours_12 == 0:
        hours_12 = 12  # إذا كانت الساعة 0، نعيدها إلى 12

    # تنسيق الوقت الجديد
    formatted_time = f"{hours_12:02}:{minutes:02}:{seconds:02}"

    # إرسال الرد إلى المستخدم
    bot.reply_to(message, f"<strong>الوقت الآن هو: <code>{formatted_time}</code> {period}</strong>", parse_mode="HTML")

# دالة لتحديد الفترة الزمنية (صباحًا أو مساءً)
def current_period(hours):
    if hours >= 12:
        return "مساءً"
    else:
        return "صباحاً"

@bot.message_handler(func=lambda message: message.text == "التاريخ")
def send_time(message):
    # الحصول على التاريخ الميلادي الحالي
    current_date = datetime.now()
    gregorian_date = current_date.strftime('%d/%m/%Y')

    # تحويل التاريخ الميلادي إلى هجري
    hijri_date = Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()
    hijri_formatted = f"{hijri_date.day}/{hijri_date.month}/{hijri_date.year}"

    # الرد على المستخدم بالتاريخ الميلادي والهجري مع نص غامق
    bot.reply_to(message, f"<b>التاريخ الميلادي:</b> {gregorian_date}\n<b>التاريخ الهجري:</b> {hijri_formatted}", parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "دي")
def bad_dy(message):
    db = "ولي"
    bs = "اخلاق زربه"
    mn = "امشيك بيها راس مطي"
    rad = random.choice([db, bs, mn])
    bot.reply_to(message, f"{rad}")

@bot.message_handler(func=lambda message: message.text == "يلا دي")
def bad_dy2(message):
    db = "ولي"
    bs = "اخلاق زربه"
    mn = "امشيك بيها راس مطي"
    rad = random.choice([db, bs, mn])
    bot.reply_to(message, f"{rad}")

@bot.message_handler(func=lambda message: message.text == "بوت")
def badl_dy(message):
    db = "عمري"
    bs = "حياتي"
    rad = random.choice([db, bs])
    bot.reply_to(message, f"{rad}")

# بدء البوت





@bot.message_handler(func=lambda message: message.text == "S1")
def badli_dy(message):
    db = "ها ولاك شتريد 🗿"
    mn = "عيوني❤️"
    rad = random.choice([db, mn])
    bot.reply_to(message, f"{rad}")

@bot.message_handler(func=lambda message: message.text == "انجب")
def badlijk_dy(message):
    user_id=message.from_user.id
    chat_id=message.chat.id
    if is_admin(chat_id, user_id):
        jd="دگلي انجب فوق مااني منطيك رتبة ادمن🫵😌"
        he="دنجب"
        rad=random.choice([jd, he])
        bot.reply_to(message,f"{rad}")
    else:
        db = "بطيزك حب 😹😹😹😹"
        mn = "ولي وللك"
        rad = random.choice([db, mn])
        bot.reply_to(message, f"{rad}")
import telebot
from telebot.types import ChatMember

# إدخال التوكن الخاص بالبوت


# دالة للتحقق من أن الشخص الذي يرسل هو أدمن
def is_admin(chat_id, user_id):
    member = bot.get_chat_member(chat_id, user_id)
    return member.status in ['administrator', 'creator']

# دالة رفع شخص إلى أدمن
@bot.message_handler(func=lambda message: message.text == "رفع ادمن" or "اد")
def promote(message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    # التحقق من أن الشخص الذي أرسل الأمر هو أدمن
    if is_admin(chat_id, from_user_id):
        # التحقق من أن هناك رد على رسالة
        if message.reply_to_message:
            user_id_to_promote = message.reply_to_message.from_user.id

            try:
                # رفع الشخص إلى أدمن
                bot.promote_chat_member(
                    chat_id,
                    user_id_to_promote,
                    can_change_info=True,
                    can_delete_messages=True,
                    can_invite_users=True,
                    can_restrict_members=True,
                    can_pin_messages=True,
                    can_promote_members=True
                )
                bot.reply_to(message, f"تم رفع {message.reply_to_message.from_user.first_name} إلى أدمن!")
            except Exception as e:
                bot.reply_to(message, f"حدث خطأ: {e}")
        else:
            bot.reply_to(message, "يرجى الرد على رسالة الشخص الذي تريد رفعه.")
    else:
        bot.reply_to(message, "فقط الأدمن يمكنهم استخدام هذا الأمر.")
@bot.message_handler(func=lambda message: message.text == "تنزيل ادمن")
def promote(message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id

    # التحقق من أن الشخص الذي أرسل الأمر هو أدمن
    if is_admin(chat_id, from_user_id):
        # التحقق من أن هناك رد على رسالة
        if message.reply_to_message:
            user_id_to_promote = message.reply_to_message.from_user.id

            try:
                # رفع الشخص إلى أدمن
                bot.promote_chat_member(
                    chat_id,
                    user_id_to_promote,
                    can_change_info=False,
                    can_delete_messages=False,
                    can_invite_users=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False
                )
                bot.reply_to(message, f"تم تنزيل هذا شخص من رتبة ادمن {message.reply_to_message.from_user.first_name}")
            except Exception as e:
                bot.reply_to(message, f"حدث خطأ: {e}")
        else:
            bot.reply_to(message, "يرجى الرد على رسالة الشخص الذي تريد رفعه.")
    else:
        bot.reply_to(message, "فقط الأدمن يمكنهم استخدام هذا الأمر.")

# دالة لمعالجة الرسائل التي تحتوي على "سورة الفاتحة"
@bot.message_handler(func=lambda message: message.text == "سورة الفاتحة")
def send_audio1(message):
    # إنشاء زر تفاعلي
    hn = types.InlineKeyboardButton(text="💋", url="https://t.me/ismhodi")
    ss = types.InlineKeyboardMarkup(row_width=1)
    ss.add(hn)
    bot.send_audio(message.chat.id, audio='https://t.me/ismhodi/50', reply_markup=ss)
@bot.message_handler(func=lambda message: message.text == "سورة البقرة")
def send_audio(message):
    if  message.chat.type=="soupergroup":
        
        hj=types.InlineKeyboardButton(text="💋",url="https://t.me/ismhodi")
        bn=types.InlineKeyboardMarkup(row_width=1)
        bn.add(hj)
        bot.send_audio(message.chat.id, audio="https://t.me/ismhodi/49", reply_markup=bn)
      
    else:
        
        pass

    


bot.infinity_polling(none_stop=True)