data = "90,45,66,77,ab,89"
marks = data.split(",")
print(marks)
valid_marks = filter(str.isdigit, marks)
print(sum(map(int, valid_marks)))
