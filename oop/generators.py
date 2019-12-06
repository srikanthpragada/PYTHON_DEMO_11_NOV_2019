def factors(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            yield i


def duplicates(s):
    dups = []
    for c in s:
        if c not in dups:
            if s.count(c) > 1:
                dups.append(c)
                yield c


for f in factors(125):
    print(f)

for c in duplicates("Programming in Python"):
    print(c)