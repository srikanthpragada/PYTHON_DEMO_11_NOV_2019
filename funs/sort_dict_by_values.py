d = {1: 10, 2: 5, 4: 20, 3: 2}

for t in sorted(d.items(), key=lambda t: t[1]):
    print(t)

