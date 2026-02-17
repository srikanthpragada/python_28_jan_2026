# Prints a table using command-line arguments
import sys

if len(sys.argv) < 2:
    print("Usage : python print_table.py  number  [length]")
    exit()

num = int(sys.argv[1])

# If length is given as 3rd param then we use it otherwise it is set to 10
length = 10
if len(sys.argv) > 2:
    length = int(sys.argv[2])

for i in range(1, length + 1):
    print(f"{num:5}  * {i:2} = {num * i:8}")


