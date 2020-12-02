import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Avengers:_Endgame")
soup = bs4.BeautifulSoup(res.text, "lxml")
# print(soup)

first_item = soup.select('.toctext')[0]

# print(first_item)

for item in soup.select('.toctext'):
    print(item.text)
