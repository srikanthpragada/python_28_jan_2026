# Take a number and display factors other than 1 and itself

num = int(input("Enter a number:"))

sum = 0
for n in range(1, num // 2 + 1):
    if num % n == 0:
        sum += n

if sum == num:
    print("Perfect")
else:
    print("Not perfect")


