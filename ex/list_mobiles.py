import re

f = open("mobiles.txt","rt")
mobiles  = set()
for line in f:
    parts = re.split("[ ;,:]",line)
    for p in parts:
        if re.fullmatch("\d{10}",p):  # true if not None
            mobiles.add(p)


for p in sorted(mobiles):
    print(p)

