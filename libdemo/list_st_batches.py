import requests
from bs4 import BeautifulSoup
import sys

resp = requests.get("http://www.srikanthtechnologies.com")
if resp.status_code != 200:
    print("Sorry! Could not retrieve data from website!")
    sys.exit(1)

bs = BeautifulSoup(resp.text, "html.parser")

table = bs.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView2'})
if table is None:
    print('Sorry! Could not get details!')
    sys.exit(1)

for tr in table.find_all("tr")[1:]:
    cols = tr.find_all("td")
    print(f"{cols[0].text:30} {cols[2].text:10} {cols[1].text}")
