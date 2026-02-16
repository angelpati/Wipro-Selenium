from bs4 import BeautifulSoup
import requests
url ="https://www.fracsdxb.com/"
headers={
    #user - agent who is making the request
    "User-Agent" :"Mozilla/5.0"

}
response = requests.get(url,headers=headers)
print(response.status_code)
soup=BeautifulSoup(response.text,features="html.parser")
print(soup)
print("\nFirst H1:",soup.find("h1"))
print("First H2:",soup.find("h2"))
print("First H3:",soup.find("h3"))

# for price
#to check what is in stock



