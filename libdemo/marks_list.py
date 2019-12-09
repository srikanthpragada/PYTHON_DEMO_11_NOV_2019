# Print student name, total marks and avg marks for marks.txt
import sys

student_marks = {}
try:
    f = open("marks.txt", "rt")
except:
    print("Sorry! File not found!")
    sys.exit(1)

for line in f.readlines():
    parts = line.strip("\n").split(",")
    # ignore invalid line
    if len(parts) < 2:
        continue

    name = parts[0]
    del parts[0]
    student_marks[name] = [int(v) for v in parts if v.isdigit()]

# print(student_marks)

for name, marks in sorted(student_marks.items()):
    total = sum(marks)
    avg = total / len(marks)
    print(f"{name:10} {','.join(map(str, marks)):10} {total:4} {avg:.2f}")

f.close()
