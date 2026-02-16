#Write a simple program to parse a small HTML string.

from bs4 import BeautifulSoup
import requests
html_doc="""<html>
          <head><title>Test Page</title></head>
          <body>
          <h1>Welcome</h1>
          <p>This is a paragraph.</p>
          </body></html>"""

#parse the html
soup=BeautifulSoup(html_doc,features="html.parser")
#html code is printed
print (soup)
#to find title, head, and paragraph
print(soup.find("title"))
print(soup.find("h1"))
print(soup.find("p"))
#for links
links=soup.find_all("a")
for link in links:
    print(link.get("href"))

print(soup.prettify())





