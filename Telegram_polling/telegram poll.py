from telethon.tl.types import InputMediaPoll, Poll, PollAnswer
from telethon import TelegramClient
import asyncio


print("\n" + "#" * 15 + " WELCOME TO TELEGRAM POLLS " + "#" * 15)

async def main():
    accounts=[API ID,"API HASH"]
    
    client= TelegramClient('SESSION ACCOUNT ', accounts[0], accounts[1])    
    await client.start()

    
   await client.send_message("YOUR CHANNEL JOIN LINK",file=InputMediaPoll(
        poll=Poll(
            id=12345567, # create the Poll id
            question="Is it 2020?", #edit the question here 
            answers=[PollAnswer('Yes', b'1'), PollAnswer('No', b'2')] #edit add options here
        )
        ))
   
    

asyncio.run(main())
