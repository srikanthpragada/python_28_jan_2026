
st = "89,34,55,75,79"
marks = []
for v in st.split(","):
    marks.append( int(v))

print(sum(marks), min(marks), max(marks))
