names = ['Scott', 'Micheal', 'Geroge', 'Kevin', 'Mark']

with open("names.txt", "wt") as f:  # w-write, t-text
    for name in names:
        f.write(name + "\n")


