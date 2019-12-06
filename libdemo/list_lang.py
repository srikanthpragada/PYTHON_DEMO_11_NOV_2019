with open("langs.txt", "rt") as f:
    for idx, line in enumerate(f):
        print(f"{idx + 1:03}:{line}", end='')
