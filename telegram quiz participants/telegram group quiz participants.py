from telethon import TelegramClient,functions, types
import json  
import asyncio
import os

print("\n" + "#" * 15 + " WELCOME TO TELEGRAM QUIZ SCRAPPER " + "#" * 15)

async def main():
    print("logging in")
    client= TelegramClient('SESSION FILE NAME', API ID, "API HASH")      
    await client.start()

    print("getting channel info..")
    channel_names=['dailygkquiz24','ALL_EXAM_QUIZ_HUB','EXAMHUB_2020']

    print("setting up the folder")
    users={}
    current=os.getcwd()+"\\QUIZ"
    try:
        os.mkdir(current)
    except:
        print("QUIZ folder exists")
        
    os.chdir(current)
    
    for channel in channel_names:
        channel_entity= await client.get_entity(channel)

        print("Reading the messages from the group..",channel)

        i=0
        
        async for m in client.iter_messages(channel_entity,10000):
            i+=1
            print(i,"/10000.....",end='\r')
            try:
            
                result=await client(functions.messages.GetPollVotesRequest(channel_entity,m.id,100))

                for user in result.users:
                    if user.bot == False:
                        name=user.first_name + ' ' + user.last_name
                        
                        if name in users:
                            users[name]['count']+=1
                        else:
                            users[name]={'first_name':user.first_name,
                                         'last_name':user.last_name,
                                         'count':0,
                                         'username':user.username,
                                         'phone':user.phone,
                                         'id':user.id,
                                         'access_hash':user.access_hash}
                              
            except:
                continue

    
    out_file = open("users.json", "w")      
    json.dump(users, out_file, indent = 6)          
    out_file.close()  
        
        
    await client.disconnect()
   
asyncio.run(main())
