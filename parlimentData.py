import requests
import GNewsData
link= "https://data.gov.in/node/85986/datastore/export/json"
page = requests.get(link)
data= page.json()['data']
for person in data: 
    name= person[2].strip()
    print(name,",",person[5])
    GNewsData.getNews(name)
