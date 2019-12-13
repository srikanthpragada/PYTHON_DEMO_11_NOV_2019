import requests
import sys

def get_country_info(countries, code):
    for c in countries:
        if c['alpha3Code'] == code:
            return c
    else:
        return None


resp = requests.get("https://restcountries.eu/rest/v2/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    sys.exit(0)

countries = resp.json()  # list of dict
india = get_country_info(countries,'IND')

for b in india['borders']:
    c = get_country_info(countries,b)
    print(c['name'])


