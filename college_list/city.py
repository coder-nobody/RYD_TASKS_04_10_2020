import requests
from bs4 import BeautifulSoup
import pandas
import os
import multiprocessing as mp


def datacitywise(city,courses):
    data=[]
    
    url='https://www.sulekha.com'
    for course in courses:
        try:
            r = requests.get(url+'/'+course+'/'+city)
            c = r.content
            print((' COLLECTING DATA FROM: '+city+' COLLEGES FOR: '+course+(" "*20)),end='\r')
            soup = BeautifulSoup(c, 'html.parser')
            qus = soup.find_all('div', {'class': 'head'})
            for i in qus:
                d={}
                if i.find('h3')!=None:
                    d['NAME'] = i.find('h3').text
                if i.find('span', {'class': 'location'})!=None:
                    addr=i.find('span', {'class': 'location'}).text
                    if addr.startswith('Also Servicing'):
                        continue
                    else:
                        d['LOCATION'] = addr
                if i.find('em')!=None:
                    d['COURSES'] = i.find('em').text
                if i.find('b', {'class': "icon-phone f-icon isbvn"})!=None:
                    d['CONTACT NO.'] = i.find('b', {'class': "icon-phone f-icon isbvn"}).text+"_"
                if d:
                    data.append(d)
        except:
            continue
    print("\n DATA COLLECTION COMPLETE....\n NOW WRITTING DATA TO FILE : "+city+'_colleges.csv\n')
    df = pandas.DataFrame(data)
    df.to_csv(city+'_colleges.csv')



if __name__ == "__main__":
    print("CREATING INDIA FOLDER...")

    os.mkdir(os.getcwd()+"\\INDIA")
    os.chdir(os.getcwd()+"\\INDIA")
    url='https://www.sulekha.com'

    r = requests.get(url)
    c = r.content

    soup = BeautifulSoup(c, 'html.parser')
    cities = soup.find(id="topCities").get('value').lower().split(',')
    cities.remove("india")

    src=(soup.find(class_="edu-training").parent).find(class_="menu-container").find_all('a')
    courses=['engineering-colleges']
    l=len(url)+1
    for x in src:
        lk=str(x.get('href'))
        courses.append(lk[l:lk.rfind('/')])

    print(" COLLECTING DATA PLEASE WAIT...")
    for x in range(0,len(cities),25):     
        n=0
        while n<25 and (n+x)<len(cities):
            p = mp.Process(target=datacitywise, args=(cities[x+n],courses ))
            n+=1
            p.start()
        p.join()
        

#print("\n ALL DATA SUCCESSFULLY COLLECTED........\n TERMINATING PROGRAM..............:)")

