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
    channel_names=['dailygkquiz24','ALL_EXAM_QUIZ_HUB','EXAMHUB_2020']

    print("setting up the folder")
    
    current=os.getcwd()+"\\QUIZ"
    try:
        os.mkdir(current)
    except:
        print("QUIZ folder exists")
        
    os.chdir(current)
    
    
    for channel in channel_names:
        
        channel_entity= await client.get_entity(channel)

        print("Reading the messages from the group..",channel)
        msg={}
        sno=1
        
        try:
            async for m in client.iter_messages(channel_entity):
                
                
                try:
                    date=str(m.date.year)+'_'+str(m.date.month)+'_'+str(m.date.day)
                    p=m.media.to_dict()
                    if date == 2020_10_31:
                        print(date)
                        break
                    
                    poll=p['poll']
                    results=p['results']['results']
                    '''
                    for x in poll.items():
                        print(x)

                    for x in results:
                        print(x)
                    
                    
                    '''
                    if len(results)==0:
                        continue
                    if date in msg:
                        msg[date][sno]={"QUESTION":poll['question'],"OPTIONS":{}}
                    else:
                        msg[date]={sno:{"QUESTION":poll['question'],"OPTIONS":{}}}
                            
                    for a in poll['answers']:
                        msg[date][sno]["OPTIONS"][a['option'].decode()]=a['text']
                    for r in results:
                        if r['correct'] is True:
                            msg[date][sno]["ANSWER"]=r['option'].decode()
                        
                    sno+=1
                    
                
                except:
                    
                    continue
        except:
            print("Some ERROR OCCURED..saving the collected results in file")
            

        print("saving the data in json file..")
        
        out_file = open(channel+".json", "w")      
        json.dump(msg, out_file, indent = 6)          
        out_file.close()  
        
        print("done!!!!!!!!!")
        
   
asyncio.run(main())
