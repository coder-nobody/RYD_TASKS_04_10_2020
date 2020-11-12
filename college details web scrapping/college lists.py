import requests
#from bs4 import BeautifulSoup
#import json
import pandas

states=["Andaman and Nicobar Islands ","Andhra Pradesh ","Arunachal Pradesh ",
        "Assam ","Bihar ","Chandigarh ",
        "Chhattisgarh ","Dadra and Nagar Haveli ","Daman and Diu ",
        "Delhi ","Goa ","Gujarat ","Haryana ","Himachal Pradesh ",
        "Jammu and Kashmir ","Jharkhand ","Karnataka ","Kerala ",
        "Madhya Pradesh ","Maharashtra ","Manipur "
        ,"Meghalaya ","Mizoram ","Nagaland ","Odisha ","Orissa ","Puducherry ",
        "Punjab ","Rajasthan ","Sikkim ","Tamil Nadu ","Telangana ","Tripura ",
        "Uttar Pradesh ","Uttarakhand ","West Bengal "]
years=["2014-2015","2015-2016","2016-2017","2017-2018","2018-2019","2019-2020","2020-2021"]


u1="https://facilities.aicte-india.org/dashboard/pages/php/approvedinstituteserver.php?method=fetchdata&year="
u2="&program=1&level=1&institutiontype=1&Women=1&Minority=1&state="
u3="&course=1"
'''
url="https://facilities.aicte-india.org/dashboard/pages/angulardashboard.php#!/approved"
'''
i=0;
records=0
m=len(states)*len(years)

data=[]

for s in states:
    s=s.replace(" ","%20")
    for y in years:
        url=u1+y+u2+s+u3
        #print(url)
        i+=1
        r=requests.get(url)
        
        c=r.json()
        try:
            for _ in c:
               d={}
               d["AICTE-ID"]=_[0]
               d['NAME']= _[1]
               d['ADDRESS']= _[2]
               d['DISTRICT']=_[3]
               d['INSTUTION TYPE']=_[4]
               d['WOMEN']= _[5]
               d['MINORITY']=_[6]
               data.append(d)
               records+=1
        except:
            print(y,s," is null")
        print("Completed:", (i/m)*100,"%   records = ",records)

df = pandas.DataFrame(data)
df.to_csv('colleges.csv')


   
