from telepot.namedtuple import  ReplyKeyboardMarkup
from telepot.namedtuple import KeyboardButton as Kb
import telepot as t
#attention : dont change array '' in lists.
k=ReplyKeyboardMarkup(keyboard=[[Kb(text='start test')]])
k1=ReplyKeyboardMarkup(keyboard=[[Kb(text='try again')]])
start=0
lis=['']
lis1=['','5*6',
      '2+2','4*3','80*100','200*300','123*534','872*634','1024*2048','1*1','80-423']#stringsare the questions
lis2=['',
      ReplyKeyboardMarkup(keyboard=[[Kb(text='11'),Kb(text='30')],[Kb(text='65'),Kb(text='56')],[Kb(text='503'),Kb(text='-503')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='42'),Kb(text='0')],[Kb(text='22'),Kb(text='4')],[Kb(text='11'),Kb(text='1')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='12'),Kb(text='34')],[Kb(text='43'),Kb(text='7')],[Kb(text='10242048'),Kb(text='2^21')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='8100'),Kb(text='180')],[Kb(text='80000'),Kb(text='8000')],[Kb(text='552848'),Kb(text='872634')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='300200'),Kb(text='43')],[Kb(text='230'),Kb(text='60000')],[Kb(text='65'),Kb(text='56')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='54321'),Kb(text='534123')],[Kb(text='123534'),Kb(text='65682')],[Kb(text='12'),Kb(text='34')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='552848'),Kb(text='872634')],[Kb(text='635872'),Kb(text='65432')],[Kb(text='12'),Kb(text='34')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='10242048'),Kb(text='2^21')],[Kb(text='2^110'),Kb(text='765432')],[Kb(text='80000'),Kb(text='8000')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='0'),Kb(text='2')],[Kb(text='11'),Kb(text='1')],[Kb(text='42'),Kb(text='0')],[Kb(text='STOP THE TEST')]]),
      ReplyKeyboardMarkup(keyboard=[[Kb(text='-343'),Kb(text='343')],[Kb(text='503'),Kb(text='-503')],[Kb(text='54321'),Kb(text='534123')],[Kb(text='STOP THE TEST')]])
      ]
# about lis2 : strings are choices(to answer)
lis3=['','30','4','12','8000','60000','65682','552848','2^21','1','-343']#list of right answers
#start_time = None
users={}
def main(ms):

    #global start_time
    i = ms['chat']['id']
    
    if i in users:
        start=users[i][0]
    else:
        users[i]=[0,['']];
        start=0
    
    c = ms['text']
    try:
        print(ms['from']['first_name']+" " +ms['from']['last_name'],' : ',c)
    except:
        print(ms['from']['username'],' : ',c)
    
    
    #if c=='/start':
    if start==0:
        bot.sendMessage(i,'Test',reply_markup=k)#name of test
        
    if c=='start test' or c=='try again':
        start=1

    if start and start<12:#number of questions-2
        if c=='STOP THE TEST':
            start=0
            users[i][1]=[""]
            bot.sendMessage(i,"YOU EXITED THE TEST...TO RESTART AGAIN ENTER: /start")
            
        if c!='start test' and c!='try again':
            users[i][1].append(c)
        if start<11:
            bot.sendMessage(i,lis1[start],reply_markup=lis2[start])
        else:
            start=0
            co=0
            no=0
            #print(users[i][1])
            for j in users[i][1]:
                if j==lis3[co]:
                    no = no+1
                co = co+1
            users[i][1]=['']
            bot.sendMessage(ms['chat']['id'], str(' \n YOUR RESULT : '+str(no)+'/10 '),reply_markup=k1)
        if start!=0:
            start=start+1
    #else:
        #bot.sendMessage(i,"TO Start the test enter \start")
    users[i][0]=start

    
bot=t.Bot('1327789124:AAG8RCtJj7sNUXyOU06YCC5qG95ULTdCVQM')
bot.message_loop(main)
while True:
    s = 1
