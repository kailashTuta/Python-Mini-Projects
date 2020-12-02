import bs4
import requests

res = requests.get("https://en.wikipedia.org/wiki/Avengers:_Endgame")

soup = bs4.BeautifulSoup(res.text, "lxml")

print(soup.select('.thumbborder'))

poster = soup.select('.thumbborder')[0]

# print(type(poster))

print(poster['src'])
