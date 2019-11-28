names = ["Bill", "peter", "Richards", "JOE", "andy"]

for n in sorted(names, key=lambda s: s[-1]):
    print(n)
