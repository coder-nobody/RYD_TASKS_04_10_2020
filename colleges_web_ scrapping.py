import requests
from bs4 import BeautifulSoup
import csv

LINKS = ["https://www.educationforever.in/colleges/banking-finance-and-accounting",
       "https://www.educationforever.in/coaching-classes/banking-exams",
       "https://www.educationforever.in/coaching-classes/civil-services",
       "https://www.educationforever.in/coaching-classes/hobbies",
       "https://www.educationforever.in/coaching-classes/nda-cds-defence",
       "https://www.educationforever.in/coaching-classes/school-tutions",
       "https://www.educationforever.in/coaching-classes/toefl-ielts-toeic-sat-gre",
       "https://www.educationforever.in/colleges/engineering-and-science",
       "https://www.educationforever.in/colleges/banking-finance-and-accounting",
       "https://www.educationforever.in/colleges/professional-courses",
       "https://www.educationforever.in/colleges/medicine-and-health-care",
       "https://www.educationforever.in/colleges/management-and-business",
       "https://www.educationforever.in/colleges/counsellors-consultants",
       "https://www.educationforever.in/colleges/computers-it",
       "https://www.educationforever.in/colleges/arts-law-and-languages",
       "https://www.educationforever.in/colleges/animation-and-multimedia",
       "https://www.educationforever.in/schools/play-schools-primary-schools",
       "https://www.educationforever.in/schools/schools-for-blind",
       "https://www.educationforever.in/schools/secondary-higher-sec-schools",
       "https://www.educationforever.in/schools/study-abroad",
       "https://www.educationforever.in/universities/central-universities",
       "https://www.educationforever.in/universities/state-universities"]
print("Collecting links")
l=len(LINKS)
links=[]
i=1

for URL in LINKS:
    r=requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')         
    for link in soup.find_all(class_="event-title"):
        links.append(link.a.get('href'))
    print("{:.3f} % Complete....".format((i/l)*100),end="\r")
    i+=1
print("Now processsing links")

URL="https://www.educationforever.in"
sno=1
l=len(links)
with open("details.csv",'w+') as file:
    writer = csv.writer(file)
    writer.writerow(["S.NO","NAME","ADDRESS","PHONE NO.","MOBILE NO.","EMAIL","WEBSITE"])
    for link in links:
        print("{:.2f} % Complete....".format((sno/l)*100),end="\r")
        r=requests.get(URL+link)
        soup = BeautifulSoup(r.content, 'html5lib')
        data=str(soup.find(id="ContentPlaceHolder1_lbl_contact_desc")).split("<br/>")
        try:
            data.pop(-1)
            while "Pincode -" not in data[0] and "Phone -" not in data[0] :
                data.pop(0)
            if data[1]==data[-1]:
                data.append("Phone - NIL")
            if "Phone" in data[1]:
                phone=data[1][8:].replace('-',' ').replace('/',',')
            else:
                phone="NIL"
            
            if data[2].startswith("Fax"):
                data.pop(2)
            if data[2]==data[-1]:
                data.append("Mobile - NIL")
            if data[2].startswith("Mobile"):
                mob=data[2][9:].replace('-',' ').replace('/',',')
            else:
                mob="NIL"
            if data[3]==data[-1]:
                data.append("Email Id - NIL")
            if data[3].startswith("Email Id"):
                email=data[3][11:]
            else:
                email="NIL"
            if data[3]==data[-1]:
                data.append("website - NIL")
            if "website" in data[4]:
                website=data[4][10:]
            else:
                website="NIL"
            if "website" in data[-1]:
                data.append(data.pop(0))
            else:
                data[-1]=data[-1]+', '+data.pop(0)
            
            name=link[link.rfind('/')+1:].replace('-',' ').capitalize()
            writer.writerow([sno,name,data[-1],phone,mob,email,website])
            sno+=1
        except:
            sno+=1
            continue
    
