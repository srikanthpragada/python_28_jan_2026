# Take numbers until 0 is given and display sum of even numbers and odd numbers
even_total =  odd_total =  0

while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num % 2 == 0:
        even_total += num
    else:
        odd_total += num


print('Even Total =', even_total)
print('Odd Total =', odd_total)