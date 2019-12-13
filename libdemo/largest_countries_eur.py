import requests
import sys

resp = requests.get("https://restcountries.eu/rest/v2/region/europe")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    sys.exit(0)

countries = filter(lambda c: c['area'] is not None, resp.json())  # list of dict

for c in sorted(countries, key=lambda c: c['area'], reverse=True)[:5]:
    print(c['name'])
