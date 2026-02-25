with open("names.txt", "rt") as f:
    lines = list(filter(lambda l: len(l.strip()) > 0, f.readlines()))

with open("names.txt", "wt") as f:
    for line in lines:
       f.write(line)


