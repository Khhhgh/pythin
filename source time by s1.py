from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime, timedelta
import asyncio


api_id = 'هون الايبي ايدي'
api_hash = 'حط هون الايبي هاش'
phone_number = 'حط رقمك هون'


client = TelegramClient('session_name', api_id, api_hash)

async def update_profile_name():
    await client.start(phone_number)
    while True:

        now = datetime.utcnow() + timedelta(hours=3)  
        current_time = now.strftime("%I:%M %p")  
        await client(UpdateProfileRequest(first_name=current_time))
        

        await asyncio.sleep(60)

with client:
    client.loop.run_until_complete(update_profile_name())