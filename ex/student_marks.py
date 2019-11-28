

students = {}

while True:
    rollno = int(input("Enter rollno [0 to stop] :"))
    if rollno == 0:
        break

    marks = int(input("Enter marks :"))
    if rollno in students:
        students[rollno].append(marks)  # add marks to existing list
    else:
        students[rollno] = [marks]  # create a new entry with rollno and marks

for rollno,marks in students.items():
    allmarks = ','.join(map(str, marks))
    print(f"{rollno:5}  {allmarks:20}  {sum(marks)}")