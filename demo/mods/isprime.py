import sys

if len(sys.argv) < 2:
    print('Sorry! Number is missing!')
    print("Usage: python isprime.py <number>")
    exit()

num = int(sys.argv[1])

prime = True
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print('Not a prime number')
        prime = False
        break

if prime:
    print('Prime number')
