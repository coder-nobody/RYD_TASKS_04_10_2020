from telethon import TelegramClient
import time
import json  
import asyncio
import os

print("\n" + "#" * 15 + " WELCOME TO TELEGRAM QUIZ SCRAPPER " + "#" * 15)

async def main():
    print("logging in")
    client= TelegramClient('SESSION FILE NAME', API ID, "API HASH")    
    await client.start()
    
    print("getting channel info..")
    channel_names=['English_tst','Gk_GS_Quiz_ZoneQuiz_For_All_Exam','Upschistoryculture','studyonlinevj','Idioms_Phrase']

    print("setting up the folder")

    current=os.getcwd()+"\\QUIZ"
    os.mkdir(current)
    os.chdir(current)
    
    for channel in channel_names:
        
        channel_entity= await client.get_entity(channel)

        print("Reading the messages from the group..",channel)
        msg={}        
        async for m in client.iter_messages(channel_entity):        
            
            try:
                date=str(m.date.year)+'_'+str(m.date.month)+'_'+str(m.date.day)
                p=m.media.to_dict()['poll']
                
                if date in msg:
                    msg[date][m.id]={"QUESTION":p['question'],"ANSWERS":[]}
                else:
                    msg[date]={m.id:{"QUESTION":p['question'],"ANSWERS":[]}}
                          
                for a in p['answers']:
                    msg[date][m.id]["ANSWERS"].append(a['text'])
                                        
            except:
                continue
            

        print("saving the data in json file..")
        
        out_file = open(channel+".json", "w")      
        json.dump(msg, out_file, indent = 6)          
        out_file.close()  
        
        print("done!!!!!!!!!")
   
asyncio.run(main())
