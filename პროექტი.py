import requests
import csv
from bs4 import BeautifulSoup

name = ['number','name','year','platform','votes','score']
with open('game.csv','w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(name)

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
}

url = 'https://steam250.com/top250'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,'html.parser')
games = soup.find_all('div',class_="appline")
for number,game in enumerate(games,start=1):
    name = game.find('span', class_="title")
    year = game.find('span',class_="date")
    score = game.find('span',class_="score")
    votes = game.find('span',class_="votes")
    platform = game.find('span',class_="platforms")
    with open('game.csv','a',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([number,name,year,platform,score,votes])
print(f"done writing {len(games)} game.csv")