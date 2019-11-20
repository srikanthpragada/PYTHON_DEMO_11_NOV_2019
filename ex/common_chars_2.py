# Display all common chars in 5 names

names = ['Java', 'JavaScript', 'Kava', 'ada', 'cobol']
common = None
for name in names:
    if common is None:  # first name
        common = set(name)
    else:
        common = common.intersection(set(name))

print("Common Chars : ", common)
