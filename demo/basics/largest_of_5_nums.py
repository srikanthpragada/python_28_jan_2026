# Take 5 numbers and display largest

largest = 0
for i in range(5):
    n = int(input("Enter a number :"))
    if n > largest:
        largest = n

print('Largest is', largest)

