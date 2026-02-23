
try:
    num = int(input("Enter number :"))
    print(100 / num)
except ValueError:
    print('Invalid input. Cannot be converted to int')
else:
    print('Done')
finally:
    print('Finally')


print('The End')


