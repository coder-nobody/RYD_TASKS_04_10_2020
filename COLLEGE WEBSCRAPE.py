import requests
from bs4 import BeautifulSoup
import pandas

data = []
w = ['https://www.coachingindians.com/coaching-class-in-mumbai.html', 'https://www.coachingindians.com/coaching-class-in-delhi.html', 'https://www.coachingindians.com/coaching-class-in-kolkata.html']
for x in w:
    r = requests.get(x)
    c = r.content

    soup = BeautifulSoup(c, 'html.parser')
    qus = soup.find('p', {'class': 'text t001'})
    q = str(qus).replace('\n', '').replace('\t', '').replace('</p>', '').replace('<b>', '').replace('</b>', '').replace('<hr color="#326732"/>', '').replace('<li>', '').replace('<ul class=""text t001"">', '')
    s = q.split('<p class="text t001">')
    for i in s:
        d = []
        pg = i.split('<br/>')
        for j in pg:
            d.append(j)
        data.append(d)
df = pandas.DataFrame(data)
df.to_csv('op.csv')


