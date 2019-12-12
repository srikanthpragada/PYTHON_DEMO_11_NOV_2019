import requests
import sys

user = input("Enter git username: ")
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print("Sorry! Could not get details for user!")
    sys.exit(0)

details = resp.json()
for k,v in details.items():
   print(f"{k:20} {v}")
