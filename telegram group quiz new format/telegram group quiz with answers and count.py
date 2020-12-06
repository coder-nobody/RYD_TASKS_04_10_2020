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
    
    
    channel='dailygkquiz24'
    
    print("setting up the folder")
    
    current=os.getcwd()+"\\QUIZ"
    try:
        os.mkdir(current)
    except:
        print("QUIZ folder exists")
        
    os.chdir(current)
    
    while(True):
        print("choose from the choices")  
        print("1. ENTER THE CHANNEL NAME AND SCRAP QUIZ")
        try:
            ch=int(input("2. EXIT THE PROGRAM..\n CHOOSE 1 OR 2 ONLY.."))
        except:
            print("INCORRECT DATA ENTERED...\n\n",'._._'*25)
            continue
        if ch==1:
            
            try:
                channel=input("\nENTER THE CHANNEL NAME TO SCRAP DATA..")
                print("Validating data")
                channel_entity= await client.get_entity(channel)
                print("Validation sucessful..")
            except:
                print("incorrect channel name...\n you need to enter again\n\n\n",'.'*60)
                continue
            
            print("Reading the messages from the group..",channel)
            msg={}
            sno=1
            
            try:
                async for m in client.iter_messages(channel_entity,1000):
                    
                    
                    try:
                                                
                        p=m.media.to_dict()
                        
                        poll=p['poll']
                        results=p['results']['results']
                        print(poll)
                        print(results)
                        if len(results)==0:
                            continue
                        
                        msg[sno]={"QUESTION":poll['question'],"OPTIONS":{}}
                        
                                
                        for a in poll['answers']:
                            msg[sno]["OPTIONS"]['op'+str(int(a['option'].decode())+1)]=[a['text']]

                        for r in results:
                            msg[sno]["OPTIONS"]['op'+str(int(r['option'].decode())+1)].append(r['voters'])
                            if r['correct'] is True:
                                msg[sno]["ANSWER"]='op'+str(int(r['option'].decode())+1)
                            
                            
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

        elif ch==2:
            print("Exiting the program")
            await client.disconnect()
            break
        else:
            print("wrong choice.....\nchoose 1 or 2 only\n\n\n\n\n",'-'*50)
            continue
            
            
  
asyncio.run(main())
