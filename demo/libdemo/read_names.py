f = open("names.txt", "rt")

for line in f.readlines():
   print(line.strip())  # print(line, end = '')

f.close()
