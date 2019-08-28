import requests, zipfile, io

i=1
#choose year
year='2019'
#Months required
mons=['JAN','FEB','MAR','APR','MAY','JUN',"JUL","AUG"] 
while len(mons) >0:
    mon=mons.pop()
    print(mon)
    while i<32:

        if i<10:
            r = requests.get('https://www.nseindia.com/content/historical/EQUITIES/'+year+'/'+str(mon)+'/cm0'+str(i)+str(mon)+year+'bhav.csv.zip')
            if len(r.content)<300:

                i+=1
            else:

                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(path='YOUR DATA PATH')
                i+=1
        else:   
            r = requests.get('https://www.nseindia.com/content/historical/EQUITIES/'+year+'/'+str(mon)+'/cm'+str(i)+str(mon)+year+'bhav.csv.zip')
            if len(r.content)<300:
                i+=1
            else:
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(path='YOUR DATA PATH')
                i+=1
    i=0

