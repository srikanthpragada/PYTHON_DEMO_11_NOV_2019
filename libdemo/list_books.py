import requests
import sys

resp = requests.get("http://test.srikanthpragada.com/api/books")
if resp.status_code != 200:
    print("Sorry! Could not get details of books!")
    sys.exit(0)

books = resp.json()  # list of dict
for b in sorted(books, key=lambda d: d['Price'], reverse=True)[:5]:
    print(f"{b['Title']:50} {b['Price']}")
