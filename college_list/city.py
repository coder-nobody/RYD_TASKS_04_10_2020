import requests
from bs4 import BeautifulSoup
import pandas
import os

os.mkdir(os.getcwd()+"\\INDIA")
os.chdir(os.getcwd()+"\\INDIA")

cities=['hyderabad','chennai','mumbai','bangalore','kolkata','pune','delhi','ahmedabad']
courses=['engineering-colleges','mbbs-colleges','hotel-management-degree-courses','mba-colleges','pharmacy-colleges','nursing-colleges','aviation-colleges']
url='https://www.sulekha.com'
print(" COLLECTING DATA PLEASE WAIT...")
for city in cities:
    data=[]
    for course in courses:
        r = requests.get(url+'/'+course+'/'+city)
        c = r.content
        print((' COLLECTING DATA FROM: '+city+' COLLEGES FOR: '+course),end='\r')
        soup = BeautifulSoup(c, 'html.parser')
        qus = soup.find_all('div', {'class': 'head'})
        for i in qus:
            d={}
            if i.find('h3')!=None:
                d['NAME'] = i.find('h3').text
            if i.find('span', {'class': 'location'})!=None:
                d['LOCATION'] = i.find('span', {'class': 'location'}).text
            if i.find('em')!=None:
                d['COURSES'] = i.find('em').text
            if i.find('b', {'class': "icon-phone f-icon isbvn"})!=None:
                d['CONTACT NO.'] = i.find('b', {'class': "icon-phone f-icon isbvn"}).text+"_"
            if d:
                data.append(d)
    print("\n DATA COLLECTION COMPLETE....\n NOW WRITTING DATA TO FILE : "+city+'_colleges.csv\n')
    df = pandas.DataFrame(data)
    df.to_csv(city+'_colleges.csv')
print("\n ALL DATA SUCCESSFULLY COLLECTED........\n TERMINATING PROGRAM..............:)")

