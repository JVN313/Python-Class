from bs4 import BeautifulSoup
import requests
site = requests.get("https://pokemondb.net/pokedex/scizor").text
source = requests.get("http://coreyms.com").text
mysite = requests.get("https://jvn313.github.io").text
soup = BeautifulSoup(source, "lxml")
soupP = soup.prettify()

article = soup.find("article")
summary = article.find("div", class_="entry-content").span
video = summary.find("iframe", class_="youtube-player")['src']
print(video)

