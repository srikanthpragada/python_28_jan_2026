
names = ['Scott', 'Micheal', 'Geroge', 'Kevin', 'Mark']
f = open("names.txt", "wt")   # w-write, t-text

for name in names:
    f.write(name + "\n")

f.close()
