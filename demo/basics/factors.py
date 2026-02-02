# Take a number and display factors other than 1 and itself

num = int(input("Enter a number:"))

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n)


