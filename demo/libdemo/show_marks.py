
students = []
with open("marks.txt", "rt") as f:
    for line in f.readlines():
        parts = line.strip().split(",")
        if len(parts) < 2:  # ignore line when it doesn't have enough data
            continue

        name = parts[0]
        valid_marks = list(filter(str.isdigit, parts[1:]))
        total_marks = sum(map(int, valid_marks))
        len_marks = len(valid_marks)
        students.append( (name, total_marks,total_marks/len_marks ))


for name, total, average in sorted(students, key = lambda t : t[2]):
    print(f"{name:20}  {total:3}  {average:6.2f}")






