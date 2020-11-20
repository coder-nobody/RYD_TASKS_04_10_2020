from telethon import TelegramClient,errors  
import time
import json  
import asyncio

print("\n" + "#" * 15 + " WELCOME TO TELEGRAM CHATS SCRAPPER " + "#" * 15)


async def main():
    print("logging in")
    
    client= TelegramClient('SESSION FILE', API Id, "API HASH")    
    await client.start()
    
    print("getting channel info..")
    
    channel_username='Study_General_Current_Affairs'
    channel_entity= await client.get_entity(channel_username)
    
    print("Reading the messages from the group..")
    msg={}
    async for m in client.iter_messages(channel_entity):        
        date=str(m.date.year)+'_'+str(m.date.month)+'_'+str(m.date.day)
        if date in msg:
            msg[date][m.id]={"MESSAGE":m.message}
        else:
            msg[date]={m.id:{"MESSAGE":m.message}}

    print("saving the data in json file..")       
    out_file = open("myfile.json", "w")      
    json.dump(msg, out_file, indent = 6)          
    out_file.close()  

    print("done!!!!!!!!!")
    
asyncio.run(main())
