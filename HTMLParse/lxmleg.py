import requests
from lxml import html

url = "https://news.ycombinator.com"

response = requests.get(url, timeout=10)

data = html.fromstring(response.content)

#links
links = data.xpath("//a/@href")
print(links)

#links + URLs
links = data.xpath("//a")
for link in links:
    print(link.text)
    print(link.get("href"))
#extract the data using class name

tree = html.fromstring(response.content)

titles = tree.xpath("//span[@class='titleline']/a/text()")

for t in titles:
    print(t)

