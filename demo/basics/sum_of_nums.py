# Take either 5 numbers or until 0 is given and display sum of numbers

total = 0

for n in range(5):
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    total += num

print('Total =', total)