import requests
import json
from bs4 import BeautifulSoup
url="https://quotes.toscrape.com/"
response=requests.get(url)
soup=BeautifulSoup(response.text, "lxml")
Quotes=soup.find_all('span', class_='text')
authors=soup.find_all('small', class_="author")
data=dict()
for i in range(len(Quotes)):
    data[authors[i].text]=Quotes[i].text


with open ("base.json", 'w', encoding="utf-8") as file:
    json.dump(data,file)

