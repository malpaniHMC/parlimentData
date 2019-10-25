from bs4 import BeautifulSoup
import requests

def getNews(newsItem):
    link= "https://news.google.com/rss/search?q="+urlify(newsItem)+"&hl=en-US&gl=US&ceid=US:en"
    page = BeautifulSoup(requests.get(link).content)
    items= page.find_all('item')
    for item in items:
        print(item.title)
    return items

def urlify(string_in): 
    return string_in.replace(" ","%20")
LOL.
