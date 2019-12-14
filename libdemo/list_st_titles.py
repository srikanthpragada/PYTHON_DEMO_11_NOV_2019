import requests
from bs4 import BeautifulSoup

resp  = requests.get("http://www.srikanthtechnologies.com/rss.xml")
bs = BeautifulSoup(resp.text,"xml")

for item in bs.find_all("item"):
    title = item.find("title")
    print(title.text.strip())