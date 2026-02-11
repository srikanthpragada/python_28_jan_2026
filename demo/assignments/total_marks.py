data = [(1, 90), (1, 59), (3, 55), (2, 88), (3, 58)]
students = {}

for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks

print(students)
