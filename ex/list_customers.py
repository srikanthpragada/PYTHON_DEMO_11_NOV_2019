import re

f = open("customers.txt","rt")
customers = {}
for line in f:
    name = re.search("[A-Za-z ]+",line)
    if name is None:
        continue

    phone = re.search("\d+", line)
    if phone is None:
        continue
    # found name and phone, so add them to dict
    customers[name.group(0).strip()] = phone.group(0)

for n,p in sorted(customers.items()):
    print(f"{n:15} {p}")