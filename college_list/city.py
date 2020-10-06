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
    for x in range(0,len(cities),20):
        
        try:
            p1 = mp.Process(target=datacitywise, args=(cities[x],courses )) 
            p2 = mp.Process(target=datacitywise, args=(cities[x+1],courses ))
            p3=mp.Process(target=datacitywise, args=(cities[x+2],courses ))
            p4=mp.Process(target=datacitywise, args=(cities[x+3],courses ))
            p5=mp.Process(target=datacitywise, args=(cities[x+4],courses ))
            p6=mp.Process(target=datacitywise, args=(cities[x+5],courses ))
            p7=mp.Process(target=datacitywise, args=(cities[x+6],courses ))
            p8=mp.Process(target=datacitywise, args=(cities[x+7],courses ))
            p9=mp.Process(target=datacitywise, args=(cities[x+8],courses ))
            p10=mp.Process(target=datacitywise, args=(cities[x+9],courses ))
            p11 = mp.Process(target=datacitywise, args=(cities[x+10],courses )) 
            p12 = mp.Process(target=datacitywise, args=(cities[x+11],courses ))
            p13=mp.Process(target=datacitywise, args=(cities[x+12],courses ))
            p14=mp.Process(target=datacitywise, args=(cities[x+13],courses ))
            p15=mp.Process(target=datacitywise, args=(cities[x+14],courses ))
            p16=mp.Process(target=datacitywise, args=(cities[x+15],courses ))
            p17=mp.Process(target=datacitywise, args=(cities[x+16],courses ))
            p18=mp.Process(target=datacitywise, args=(cities[x+17],courses ))
            p19=mp.Process(target=datacitywise, args=(cities[x+18],courses ))
            p20=mp.Process(target=datacitywise, args=(cities[x+19],courses ))
            
            p1.start() 
            p2.start() 
            p3.start() 
            p4.start()
            p5.start() 
            p6.start()
            p7.start() 
            p8.start()
            p9.start() 
            p10.start()
            p11.start() 
            p12.start() 
            p13.start() 
            p14.start()
            p15.start() 
            p16.start()
            p17.start() 
            p18.start()
            p19.start() 
            p20.start()
            
            p1.join()          
            p2.join()
            p3.join()          
            p4.join()
            p5.join()          
            p6.join()
            p7.join()          
            p8.join()
            p9.join()          
            p10.join()
            p11.join()          
            p12.join()
            p13.join()          
            p14.join()
            p15.join()          
            p16.join()
            p17.join()          
            p18.join()
            p19.join()          
            p20.join()
        except:
            while x<len(cities):
                p = mp.Process(target=datacitywise, args=(cities[x],courses ))
                x+=1
                p.start()
                
        

#print("\n ALL DATA SUCCESSFULLY COLLECTED........\n TERMINATING PROGRAM..............:)")

