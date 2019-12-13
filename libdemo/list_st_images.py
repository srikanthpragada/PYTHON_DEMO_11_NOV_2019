import requests
from bs4 import BeautifulSoup

resp  = requests.get("http://www.srikanthtechnologies.com")

bs = BeautifulSoup(resp.text,"html.parser")

for img in bs.find_all("img"):
    src = img['src']
    if 'title' in img.attrs:
        title = img['title']
    elif 'alt' in img.attrs:
        title = img['alt']
    else:
        title = ''
    print(f"{src:50} {title}")