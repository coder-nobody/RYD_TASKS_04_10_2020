import requests
import pandas as pd
import xlrd

url="http://dce.kar.nic.in/Files%20NRR/Genenral/AISHEpendingcollegelist.xls"

r=requests.get(url)

open("banglore_colleges.xls","wb").write(r.content)
#df=pd.read_excel("banglore_colleges.xls")
wb = xlrd.open_workbook("banglore_colleges.xls")
sheet = wb.sheet_by_index(0)
print(type(sheet.cell_value(0, 0)))
data = []
for i in range(sheet.nrows):
    
    #print(sheet.cell_value(i, 1))
    d={}
    if sheet.cell_value(i, 6) == "YES":
        #for j in range(sheet.ncols):
            #print(sheet.cell_value(i, j),end="  ")
        d["Name of the State"]=sheet.cell_value(i, 2)
        d["Name of the University"]=sheet.cell_value(i, 3)
        d["Name of the College"]=sheet.cell_value(i, 4)
        d["contact Name"]=sheet.cell_value(i, 7)
        d["Phone"]=sheet.cell_value(i, 10)
        d["Mobile"]=sheet.cell_value(i, 11)
        d["Email-Id"]=sheet.cell_value(i, 12)

        data.append(d)

print(data)

df = pd.DataFrame(data)
df.to_csv('bang_collg.csv')        
    

#print(df)
'''
    
        '''
