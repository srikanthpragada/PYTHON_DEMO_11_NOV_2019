# Take marks until 0 is given and print them in sorted order
all_marks = []

while True:
    marks = int(input("Enter marks :"))
    if marks == 0:
        break

    all_marks.append(marks)

# all_marks.sort()
for m in sorted(all_marks):
    print(m)

