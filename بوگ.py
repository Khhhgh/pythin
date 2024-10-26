from telethon import TelegramClient

api_id = '25217515'
api_hash = '1bb27e5be73593e33fc735c1fbe0d855'
client = TelegramClient('leuo', api_id, api_hash)

async def main():
    await client.start()

   
    source_channel = input("ادخل قنات الي تريد تخمط منها دز يوزر مع @ : ")
    target_channel = input("ادخل يوزر قناتك مع @ : ")


    async for message in client.iter_messages(source_channel):
        
        if message.text: 
            await client.send_message(target_channel, message.text)
        elif message.photo:  
            await client.send_file(target_channel, message.photo)
        elif message.video:  
            await client.send_file(target_channel, message.video)
        elif message.document:  
            await client.send_file(target_channel, message.document)
        elif message.sticker: 
            await client.send_file(target_channel, message.sticker)
        elif message.voice:  
            await client.send_file(target_channel, message.voice)
        elif message.audio: 
            await client.send_file(target_channel, message.audio)
        elif message.poll:  
            await client.send_message(target_channel, message.poll)
        elif message.contact:  
            await client.send_message(target_channel, message.contact)
        elif message.location:  
            await client.send_message(target_channel, message.location)

with client:
    client.loop.run_until_complete(main())