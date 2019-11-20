# Display all common chars in 5 names

for i in range(5):
    name = input("Enter name : ")
    if i == 0:
        common = set(name)
    else:
        common = common.intersection(set(name))

print("Common Chars : ", common)
