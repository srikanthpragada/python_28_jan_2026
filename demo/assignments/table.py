# Print table for the given number

num = int(input("Enter a number :"))

for n in range(1, 11):
    print(f"{num:3} * {n:2} = {num * n:5}")

